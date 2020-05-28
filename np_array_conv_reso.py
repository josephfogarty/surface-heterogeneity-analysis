"""
This script will take an ice map (an array) of a certain resolution and
"decrease" this resolution by finding an average of the cells in the "tile"

NEED TO EDIT TO INCLUDE PONDS EVENTUALLY
"""

# import needed libraries
import numpy as np
import matplotlib.pyplot as plt
import os

# Colormap properties for ice, water, and pond
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
cmap = ListedColormap(['black','xkcd:off white', 'xkcd:midnight blue', 'xkcd:cyan'])
bounds = [-0.4,0.5,1.5,2.5,3.5]
norm = BoundaryNorm(bounds,cmap.N)

#%% define the converting function

# this needs to be edited if # rows is not equal to # columns

def conv_res_down(data, rows, cols):
    
    print(f"\n  Converting Resolution from {np.shape(data)[0]} to {rows}")
    
    # see if array needs to be upscaled by calculating LCM factor
    LCM_factor = int(np.lcm(new_reso,np.shape(loaded_mat)[0])/np.shape(loaded_mat)[0])
    
    # if the array needs to be upscaled
    if LCM_factor != 1:
        
        #upscale the array
        data = np.kron(data, np.ones((LCM_factor,LCM_factor)))
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
            row_sp = int(data.shape[0]/rows)
            col_sp = int(data.shape[1]/cols)
            
            # each sub area
            zz = data[i*row_sp : i*row_sp + row_sp, j*col_sp : j*col_sp + col_sp]
            
            # assign the average to  the returned matrix
            shrunk[i,j] = round(np.mean(zz))
    
    # return
    print("    Finished!\n")       
    return shrunk

#%% Import the array
    
# set parameters of chosen ice map and new resolution
ice_map = "beaufo_2000aug31a_3c.out"
new_reso = 192

# load the text file of the array
lp = os.path.join("array_text_files","observed_ice_maps","without_ponds",ice_map)
loaded_mat = np.loadtxt(lp)

# call the function
#new_shape = (new_reso,new_reso)
new_reso_mat = conv_res_down(loaded_mat, new_reso, new_reso)

# double check the values
print("unique values for original: ", np.unique(loaded_mat))
print("unique values for new: ", np.unique(new_reso_mat))

#%% Plot and save

#plot
fig = plt.figure(figsize = (7,3.5))
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(loaded_mat,cmap=cmap,norm=norm)
ax2 = fig.add_subplot(1,2,2)
ax2.imshow(new_reso_mat,cmap=cmap,norm=norm)
plt.tight_layout()

# save path for array and before/after image
sp_array = os.path.join("array_text_files","observed_ice_maps","low_reso",ice_map[:-4]+f"_{new_reso}.out")
sp_img = os.path.join("img", "observed_ice_maps",ice_map[:-4]+f"_{new_reso}_comp.jpg")

#save array as text file and image
plt.savefig(sp_img)
np.savetxt(sp_array, new_reso_mat)






