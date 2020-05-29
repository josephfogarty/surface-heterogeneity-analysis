# code to create a heterogeneous surface

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import os

# import constants and funcs
from constants import cnst
import funcs as fn

# Colormap properties for ice, water, and pond
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
cmap = ListedColormap(['xkcd:off white', 'xkcd:midnight blue'])
bounds = [0,272.15,300]
norm = BoundaryNorm(bounds,cmap.N)

# define constants - these are changed in class cnst in constants.py
Nx = cnst.Nx
Ny = cnst.Ny
ice = cnst.ice
water = cnst.water
label = cnst.label
root = cnst.root

# bounds may need to be changed depending on label
print(f"\n  Make sure bounds apply to {label}")

# save paths for text and image files for checkerboards
sp = os.path.join(root,"surfaces","checkerboard","arrays")
sp_img = os.path.join(root,"surfaces","checkerboard","img")

#### create checkerboards ####
# base pattern
base_pattern = np.array([[ice,water],[water,ice]])
# create 2x2 checkerboard
checker2 = fn.conv_np_array_reso(base_pattern,Nx)
# create 4x4 checkerboard
checker4 = fn.conv_np_array_reso(np.tile(base_pattern,(2,2)),Nx)
# create 8x8 checkerboard
checker8 = fn.conv_np_array_reso(np.tile(base_pattern,(4,4)),Nx)
# create 16x16 checkerboard
checker16 = fn.conv_np_array_reso(np.tile(base_pattern,(8,8)),Nx)

#### write arrays and images to a file ####

# save text files
np.savetxt(os.path.join(sp,f'checker2_{label}_reso{Nx}.txt'), checker2, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f'checker4_{label}_reso{Nx}.txt'), checker4, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f'checker8_{label}_reso{Nx}.txt'), checker8, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f'checker16_{label}_reso{Nx}.txt'), checker16, delimiter=' ',fmt='%.2f')

# save images of checkerboards
fig, ax = plt.subplots(1,4,figsize=(10,3))
ax[0].imshow(checker2, cmap=cmap, norm=norm)
ax[1].imshow(checker4, cmap=cmap, norm=norm)
ax[2].imshow(checker8, cmap=cmap, norm=norm)
ax[3].imshow(checker16, cmap=cmap, norm=norm)
plt.savefig(os.path.join(sp_img,f"checker_{label}_reso{Nx}_comparison"))
plt.close()

