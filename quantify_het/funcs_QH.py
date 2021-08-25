# useful functions for heterogeneity

# needed libraries
import numpy as np
from scipy import stats
from scipy.integrate import simps
from scipy.signal import argrelextrema
from libpysal.weights import lat2W
from esda.moran import Moran
from esda.join_counts import Join_Counts

##### the functions #####

def ice_fraction(surface):
    """
    This function gives the counts for ice and water for a sea-ice surface
    
    returns a dictionary of the counts and unique values
    """
    ice_stat = {}
    
    unique, counts = np.unique(surface, return_counts=True)
    for uv, count in zip(unique, counts):
        ice_stat[str(uv)+' count'] = count
    ice_stat['total count'] = np.size(surface)
    
    return ice_stat
    

def semivariogram(arr,peak=False):

    """
    This is a brute-force semivariogram code which computes the structure
    function across rows, then averages to create the semivariogram

    This function also calculates the integral length scale using the method
    outlined in Bou-Zeid et. al (2007), JAS

    arr is the 2D array to be analyzed
    peak is used for ideal patterns

    Built off of NumPy, SciPy
    """

    # range of rx
    rx_vals = np.arange(np.shape(arr)[1]//2)

    # empty list for semivar
    semivar = []

    # for each spatial translation vector
    for rx in rx_vals:

        # print rx (optional)
        rxl = len(rx_vals)
        #print(f'  Progress: {rx}/{rxl}, {rx/rxl*100:.2f}%')

        # get rolled array
        rolled = np.roll(arr,rx,axis=1)

        # calculate squared difference, average, and append to list
        semivar.append(np.mean((arr - rolled)**2))

    # now we have a list of rx values and structure function values
    # rx_val and semivar - convert semivar to array
    semivar = np.array(semivar)
    #print("    Semivariogram obtained")

    # check for all zeros in semivar
    all_zeros = not np.any(semivar)

    #### calculate integrand for integral length scale ####

    # in the (usual) case where are not zeros in the semivariogram
    if all_zeros == False:

        # calculate integral length scale via Bou-Zeid (2007)
        # but only for semivar once it reaches it's approx maximum value
        # for a periodic domain, this is done when the shift is
        # half of the domain

        # in the case where the peak is true (for ideal patterns)
        if peak == True:

            # normalized semivariogram
            semivarn = semivar/np.max(semivar)

            # calculate cutoff
            n = 0.1
            print(f"    Using PEAK method: first maxima that is {n} from maximum")

            # normalized list of local maxima
            lmax = argrelextrema(semivarn, np.greater_equal)[0]

            # compare the absolute difference between 1 and the first maxima
            for i in range(len(lmax)):
                #print(i,lmax[i])
                if abs(1.0-semivarn[lmax[i]]) <= n:
                    cutoff_location = np.where(semivarn==semivarn[lmax[i]])[0][0]
                    print(f"    Max value found at rx={lmax[i]}")
                    break

            # now cut the array and calculate integrand
            integrand = 1.0 - (semivar[:cutoff_location+1]/np.max(semivar))

            # calculate change in rx
            drx = 1.0

            # estimate integral using simpsons rule to get integral length scale
            l_p = simps(integrand, dx=drx)

            return rx_vals, semivar, l_p

        integrand = 1.0 - (semivar[:len(semivar)//2]/np.max(semivar))

        # calculate change in rx
        # should be 1 for using the arange function
        # but this might change later
        drx = 1.0

        # estimate integral using simpsons rule to get integral length scale
        l_p = simps(integrand, dx=drx)

        # now cut the array halfway and calculate integrand
        integrand = 1.0 - (semivar[:len(semivar)//2]/np.max(semivar))

        # calculate change in rx
        # should be 1 for using the arange function
        # but this might change later
        drx = 1.0

        # estimate integral using simpsons rule to get integral length scale
        l_p = simps(integrand, dx=drx)
        # l_p = np.sum(integrand)
        # print(l_p)

    # but if there are zeros,
    else:
        l_p = len(semivar)
        print("    All homogeneous in this direction, semivar is empty")

    return rx_vals, semivar, l_p



def calculate_transition_statistics(array):

    """
    This function calculates the average length of patches
    by analyzing the length of similar pixels in a row
    in the x direction

    transpose the matrix for the same calculation
    in the y direction

    inputs:
    the array to calculate thransition statistics

    outputs:
    a dictionary with...
    """

    #print(f"\n  Calculating transition statistics for array of shape {np.shape(array)}")
    # first, look for interval changes and pad with bool 1s on sides to set the
    # first interval for each row and for setting boundary wrt the next row
    p = np.ones((len(array),1), dtype=bool)
    m = np.hstack((p, array[:,:-1]!=array[:,1:], p))

    # Look for interval change indices in flattened array version
    intv = m.sum(1).cumsum()-1

    # Get index and counts
    idx = np.diff(np.flatnonzero(m.ravel()))
    count = np.delete(idx, intv[:-1])
    val = array[m[:,:-1]]

    # Get couples and setup offsetted interval change indices
    grps = np.c_[val,count]
    intvo = np.r_[0,intv-np.arange(len(intv))]

    # Finally slice and get output for each row
    out = [grps[i:j] for (i,j) in zip(intvo[:-1], intvo[1:])]

    # create list of lengths based on unique values of array
    all_length_information = {}
    for uv in np.unique(array):
        all_length_information[uv] = []
    #print(f"    Unique values for this array are: {np.unique(array)}")

    # obtain number of transitions and each transition length per row
    for i in range(len(out)):

        # get array for this row
        arr_row = out[i]

        # get unique values of 1st column
        unique = np.unique(arr_row[:,0])

        # for each unique value
        for value in unique:

            # get what rows has this unique value
            inds = np.where(arr_row == value)[0]

            # append these values to list
            for j in inds:
                all_length_information[value].append(arr_row[j,1])

    return all_length_information



def prep_periodic(surface):

    """
    This function will simply add a border around the surface array that
    represents the periodicity of the domain

    This is done for quantification methods that require information on
    the eight surrounding pixels, so that the borders may be accurately
    calculated

    surface is the 2D array to be padded
    the new size of su

    Built off of NumPy, specifically the np.pad(function)
    """

    # apply np.pad
    #print(f'\n  Adding border to surface of shape {np.shape(surface)}')
    surface_padded = np.pad(surface,pad_width=1,mode='wrap')
    #print(f'  the new shape of surface is {np.shape(surface_padded)}')

    return surface_padded



def evenness(surface):

    """
    This function calculates the evenness of a surface

    Do not apply the prep_periodic() function for this function

    inputs:
    surface - surface to calculate evenness

    outputs:
    E - the eveness of the surface
    """

    # get information on patch types and frequency
    pixel_stats = np.array(np.unique(surface, return_counts=True)).T

    # number of unique values
    n = len(pixel_stats)

    # sum of squared probabilities that each unique value is randomly chosen
    prob_sum = 0
    for unique in pixel_stats:
        prob_sum += (unique[1]/np.size(surface))**2.0

    # calculate E
    E = -100.0*np.log(prob_sum)/np.log(n)
    return E


def moran(surface):

    """
    decription here

    Returns Morans I Index for a surface
    """

    # Create the matrix of weights for rook
    w_r = lat2W(nrows=surface.shape[0],
                ncols=surface.shape[1],
                rook=True)
    
    # Create the matrix of weights for rook
    w_q = lat2W(nrows=surface.shape[0],
                ncols=surface.shape[1],
                rook=False)

    # Crate the esda Moran object
    mi_r = Moran(surface, w_r)
    mi_q = Moran(surface, w_q)

    # Verify Moran's I results
    #print(f'\n  For surface, MI = {mi.I:.2f}')
    #print(f'  p_norm = {mi.p_norm:.3e}')
    return (mi_r.I, mi_r.p_norm), (mi_q.I, mi_q.p_norm) 


def joincounts(surface):
    
    """
    Returns join-count statistics (both queen and pawn configuration) 
    for a surface
    """
    
    # Create the matrix of weights for rook
    w_r = lat2W(nrows=surface.shape[0],
                ncols=surface.shape[1],
                rook=True)
    
    # Create the matrix of weights for rook
    w_q = lat2W(nrows=surface.shape[0],
                ncols=surface.shape[1],
                rook=False)

    # Crate the esda JC object
    jc_r = Join_Counts(surface, w_r)
    jc_q = Join_Counts(surface, w_q)

    # Verify Moran's I results
    #print(f'\n  For surface, MI = {mi.I:.2f}')
    #print(f'  p_norm = {mi.p_norm:.3e}')
    return (jc_r.bb, jc_r.ww, jc_r.bw), (jc_q.bb, jc_q.ww, jc_q.bw)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
