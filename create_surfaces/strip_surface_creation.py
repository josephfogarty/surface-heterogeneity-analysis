"""
This script will create LES-ready maps for bands of ice and sea
"""

# import needed libraries
import numpy as np
import matplotlib.pyplot as plt
import os

# import constants and funcs by going up one, importing, then going back down
os.chdir(os.path.join("D:",os.sep,"surface-heterogeneity-analysis"))
from constants import cnst
#import funcs as fn
os.chdir(os.path.join("create_surfaces"))

# colormap properties for ice, water, and pond
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
print(f"\n  Make sure bounds for colorbar apply to {label}")

# save paths for text and image files for strips
sp = os.path.join(root,"surfaces","strips","arrays")
sp_img = os.path.join(root,"surfaces","strips","img")

#### create the strip arrays, par (ideal) and perp (trans) ####

# base array of all ice and water
arr_base_w = np.full((Nx,Ny),water)
arr_base_i = np.full((Nx,Ny),ice)

# for two strips
strip_02 = np.copy(arr_base_w)
strip_02[:,:Nx//2] = ice
strip_02_trans = strip_02.T

# for four strips
N = 4
strip_04 = np.copy(arr_base_w)
ind = np.arange(0,Nx,Nx//N)
values = np.resize([1,2],N)
for i, v in zip(ind,values):
    strip_04[:,i:] = v
strip_04_trans = strip_04.T

# for 8 strips
N = 8
strip_08 = np.copy(arr_base_w)
ind = np.arange(0,Nx,Nx//N)
values = np.resize([1,2],N)
for i, v in zip(ind,values):
    strip_08[:,i:] = v
strip_08_trans = strip_08.T


# for 16 strips
N = 16
strip_16 = np.copy(arr_base_w)
ind = np.arange(0,Nx,Nx//N)
values = np.resize([1,2],N)
for i, v in zip(ind,values):
    strip_16[:,i:] = v
strip_16_trans = strip_16.T


# for 32 strips
N = 32
strip_32 = np.copy(arr_base_w)
ind = np.arange(0,Nx,Nx//N)
values = np.resize([1,2],N)
for i, v in zip(ind,values):
    strip_32[:,i:] = v
strip_32_trans = strip_32.T

#### write arrays and images to a file ####

# save text files
np.savetxt(os.path.join(sp,f"constant_ice_{label}_reso{Nx}.txt"), arr_base_i, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"constant_water_{label}_reso{Nx}.txt"), arr_base_w, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_02_perp_{label}_reso{Nx}.txt"), strip_02, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_04_perp_{label}_reso{Nx}.txt"), strip_04, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_08_perp_{label}_reso{Nx}.txt"), strip_08, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_16_perp_{label}_reso{Nx}.txt"), strip_16, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_32_perp_{label}_reso{Nx}.txt"), strip_32, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_02_par_{label}_reso{Nx}.txt"), strip_02_trans, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_04_par_{label}_reso{Nx}.txt"), strip_04_trans, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_08_par_{label}_reso{Nx}.txt"), strip_08_trans, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_16_par_{label}_reso{Nx}.txt"), strip_16_trans, delimiter=' ',fmt='%.2f')
np.savetxt(os.path.join(sp,f"strip_32_par_{label}_reso{Nx}.txt"), strip_32_trans, delimiter=' ',fmt='%.2f')


# save images of strip files
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(figsize=(13, 5), ncols=5)
ax1.set_title("2 strips")
im2 = ax1.imshow(strip_02,cmap=cmap)
#fig.colorbar(im_di, ax=ax1)
ax2.set_title("4 strips")
im4 = ax2.imshow(strip_04,cmap=cmap)
#fig.colorbar(im_di_trans, ax=ax2)
ax3.set_title("8 strips")
im8 = ax3.imshow(strip_08,cmap=cmap)
#fig.colorbar(im_ds, ax=ax3)
ax4.set_title("16 strips")
im16 = ax4.imshow(strip_16,cmap=cmap)
#fig.colorbar(im_ds_trans, ax=ax4)
ax5.set_title("32 strips")
im32 = ax5.imshow(strip_32,cmap=cmap)
#fig.colorbar(im32, ax=ax5)
plt.savefig(os.path.join(sp_img,f"strip_perp_{label}_reso{Nx}_comparison"))
plt.close()

# view all four trans figures
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(figsize=(13, 5), ncols=5)
ax1.set_title("2 strips")
im2 = ax1.imshow(strip_02_trans,cmap=cmap)
#fig.colorbar(im_di, ax=ax1)
ax2.set_title("4 strips")
im4 = ax2.imshow(strip_04_trans,cmap=cmap)
#fig.colorbar(im_di_trans, ax=ax2)
ax3.set_title("8 strips")
im8 = ax3.imshow(strip_08_trans,cmap=cmap)
#fig.colorbar(im_ds, ax=ax3)
ax4.set_title("16 strips")
im16 = ax4.imshow(strip_16_trans,cmap=cmap)
#fig.colorbar(im_ds_trans, ax=ax4)
ax5.set_title("32 strips")
im32 = ax5.imshow(strip_32_trans,cmap=cmap)
#fig.colorbar(im32, ax=ax5)
plt.savefig(os.path.join(sp_img,f"strip_par_{label}_reso{Nx}_comparison"))
plt.close()
