"""
A code to change the resolution of surfaces
using the conv_array_reso code in funcs
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os

import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)

# import constants and funcs by going up one, importing, then going back down
os.chdir(os.path.join("D:",os.sep,"surface-heterogeneity-analysis"))
from constants import cnst
import funcs as fn
os.chdir(os.path.join("create_surfaces"))

# define constants - these are changed in class cnst in constants.py
label = cnst.label
root = cnst.root

# final array resolution
final_conv_reso = 200
print(f"\n  The final array resolution is {final_conv_reso}")

#### import and export path ####
lp = os.path.join(root,"modify_surfaces","to_be_converted")
sp = os.path.join(root,"modify_surfaces","completed")

# iterate through directory
for filename in os.listdir(lp):
    
    # for all filenames that are .txt files
    if filename.endswith(".txt") or filename.endswith(".gz"):
        
        # import array
        loaded_arr = np.loadtxt(os.path.join(lp,filename))
        
        # change resolution via function
        conv_arr = fn.conv_np_array_reso(loaded_arr, final_conv_reso)
        
        # check the unique values
        print(f"\n    The unique values of the converted array is {np.unique(conv_arr)}")
        for uv in np.unique(conv_arr):
            print(f"    The value {uv} occurs {np.count_nonzero(conv_arr == uv)} times")
        print(f"    The size of the array {np.shape(conv_arr)}")
        
        # save to the completed folder with the same name
        np.savetxt(os.path.join(sp,filename), conv_arr, delimiter=' ',fmt='%.3e')
        print(f"    File {filename} has been imported, converted, and saved")
        
        # testing to see if it was done correctly
        fig, ax = plt.subplots(ncols=2,figsize=(10,4))
        im0 = ax[0].imshow(loaded_arr)
        fig.colorbar(im0, ax=ax[0])
        im1 = ax[1].imshow(conv_arr)
        fig.colorbar(im1, ax=ax[1])
        plt.show()
        
plt.close('all')


print(f"\n  Finished - exiting.\n")











        