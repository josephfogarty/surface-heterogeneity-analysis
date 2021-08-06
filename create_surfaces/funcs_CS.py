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
        print(f"      Upscaling needed to LCM of {LCM_factor} - done!")

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
