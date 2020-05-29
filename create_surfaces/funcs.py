# useful functions for heterogeneity

# needed libraries
import numpy as np

#%% the functions

def conv_np_array_reso(loaded_mat, new_reso):
    
    # the new resolution is a square array - this must all be square
    rows = new_reso
    cols = new_reso
    
    print(f"\n  Converting Resolution from {np.shape(loaded_mat)[0]} to {new_reso}")
    
    # see if array needs to be upscaled by calculating LCM factor
    LCM_factor = int(np.lcm(new_reso,np.shape(loaded_mat)[0])/np.shape(loaded_mat)[0])
    
    # if the array needs to be upscaled
    if LCM_factor != 1:
        
        #upscale the array
        loaded_mat = np.kron(loaded_mat, np.ones((LCM_factor,LCM_factor)))
        print("    Upscaling needed and complete!")
    
    # if the factor equals one, no upscaling is needed
    else:
        pass
        print("    Upscaling not needed!")
    
    # the matrix to return
    shrunk = np.zeros((rows,cols))
    
    # iterate through rows and columns
    for i in range(0,rows):
        for j in range(0,cols):
            
            # get the indices
            row_sp = int(loaded_mat.shape[0]/rows)
            col_sp = int(loaded_mat.shape[1]/cols)
            
            # each sub area
            zz = loaded_mat[i*row_sp : i*row_sp + row_sp, j*col_sp : j*col_sp + col_sp]
            
            # assign the average to the returned matrix
            shrunk[i,j] = round(np.mean(zz))
    
    # return
    print("    Finished!\n")       
    return shrunk

