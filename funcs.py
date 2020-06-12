# useful functions for heterogeneity

# needed libraries
import numpy as np
from scipy import stats
from scipy.integrate import simps
from scipy.signal import argrelextrema

##### the functions #####

def conv_np_array_reso(arr, new_reso):
    
    """
    This function takes in a (square) array and changes the resolution of it
    by upscaling by a factor of the LCM of the old and new array shape,
    and then downscaling using the max of squares inside a cell
    
    loaded_mat is the array to be converted
    new_reso is the new resolution (remember this is square)
    """
    
    # the new resolution is a square array - this must all be square
    rows = new_reso
    cols = new_reso
    
    print(f"\n    Converting Resolution from {np.shape(arr)[0]} to {new_reso}")
    
    # see if array needs to be upscaled by calculating LCM factor
    LCM_factor = int(np.lcm(new_reso,np.shape(arr)[0])/np.shape(arr)[0])
    
    # if the array needs to be upscaled
    if LCM_factor != 1:
        
        #upscale the array
        arr = np.kron(arr, np.ones((LCM_factor,LCM_factor)))
        print(f"      Upscaling needed to {LCM_factor} and complete!")
    
    # if the factor equals one, no upscaling is needed
    else:
        pass
        print("      Upscaling not needed!")
    
    # the matrix to return
    shrunk = np.zeros((rows,cols))
    
    # iterate through rows and columns
    for i in range(0,rows):
        for j in range(0,cols):
            
            # get the indices
            row_sp = int(arr.shape[0]/rows)
            col_sp = int(arr.shape[1]/cols)
            
            # each sub area
            zz = arr[i*row_sp : i*row_sp + row_sp, j*col_sp : j*col_sp + col_sp]
            #print(zz)
            
            # convert to float
            #zz = zz.astype(float)
            
            # calculate the mode
            #mode_of_zz = stats.mode(zz,axis=None)[0][0]
            #print(f"  The mode is {mode_of_zz}")
            
            # assign the average to the returned matrix
            shrunk[i,j] = stats.mode(zz,axis=None)[0][0]
            #print(f"  Shrunk[i,j] = {shrunk[i,j]}, {type(shrunk[i,j])}")
    
    # return
    print("      Finished!\n")       
    return shrunk

def shuffle(arr, n_sections):
    
    """
    A code to take a numpy array and "shuffle" the values
    
    arr is the array to be shuffled
    n_sections is the size of the square tile
    """
    
    # array must be square and divisible into equal n sections
    assert arr.shape[0] == arr.shape[1]
    assert arr.shape[0]%n_sections == 0
    
    # size of tile to be shuffles
    size = arr.shape[0]//n_sections
    
    # create new array
    new_arr = np.empty_like(arr)
    
    ## randomize section's row index
    rand_indxes = np.random.permutation(n_sections*n_sections)
    for i in range(n_sections):
        
        ## randomize section's column index
        for j in  range(n_sections):

            rand_i = rand_indxes[i*n_sections + j]//n_sections
            rand_j = rand_indxes[i*n_sections + j]%n_sections

            new_arr[i*size:(i+1)*size, j*size:(j+1)*size] = \
                arr[rand_i*size:(rand_i+1)*size, rand_j*size:(rand_j+1)*size]

    return new_arr


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
    rx_vals = np.arange(np.shape(arr)[1])
    
    # empty list for semivar
    semivar = []
    
    # for each spatial translation vector
    for rx in rx_vals:
        
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












