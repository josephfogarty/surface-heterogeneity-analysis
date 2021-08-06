# useful functions for heterogeneity

# needed libraries
import numpy as np
from scipy import stats
from scipy.integrate import simps
from scipy.signal import argrelextrema

##### the functions #####

def semivariogram(arr,peak=False):

    """
    This is a brute-force semivariogram code which computes the structure
    function across rows

    This function also calculates the integral length scale using the method
    outlined in Bou-Zeid et. al (2007), JAS

    arr is the 2D array to be analyzed

    Built off of NumPy
    """

    # range of rx
    rx_vals = np.arange(np.shape(arr)[1]//2)

    # empty list for semivar
    semivar = []

    # for each spatial translation vector
    for rx in rx_vals:

        # print rx (optional)
        rxl = len(rx_vals)
        print(f'  Progress: {rx}/{rxl}, {rx/rxl*100:.2f}%')

        # get rolled array
        rolled = np.roll(arr,rx,axis=1)

        # calculate squared difference, average, and append to list
        semivar.append(np.mean((arr - rolled)**2))

    # now we have a list of rx values and structure function values
    # rx_val and semivar - convert semivar to array
    semivar = np.array(semivar)
    print("    Semivariogram obtained")

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
        # l_p = np.sum(integrand)
        # print(l_p)


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

    print(f"\n  Calculating transition statistics for array of shape {np.shape(array)}")
    #calculate transition scales and lists
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
    print(f"    Unique values for this array are: {np.unique(array)}")

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
