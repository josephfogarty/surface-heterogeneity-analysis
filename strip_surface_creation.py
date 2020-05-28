"""
This script will create LES-ready maps for bands of ice and sea
"""

# import needed libraries
import numpy as np
import matplotlib.pyplot as plt
import os

# colormap properties for ice, water, and pond
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
cmap = ListedColormap(['xkcd:off white', 'xkcd:midnight blue'])
bounds = [-0.4,0.5,1.5,2.5,3.5]
norm = BoundaryNorm(bounds,cmap.N)

#%% parameters

# representative values
ice = 1
sea = 2

#shape
Nx = 64
Ny = Nx

#%% create the arrays

# base array of all ice
arr_base = np.full((Nx,Ny),sea)

# for two strips
strip_02 = np.copy(arr_base)
strip_02[:,:Nx//2] = ice
strip_02_trans = strip_02.T

# for four strips
N = 4
strip_04 = np.copy(arr_base)
ind = np.arange(0,Nx,Nx//N)
values = np.resize([1,2],N)
for i, v in zip(ind,values):
    strip_04[:,i:] = v
strip_04_trans = strip_04.T

# for 8 strips
N = 8
strip_08 = np.copy(arr_base)
ind = np.arange(0,Nx,Nx//N)
values = np.resize([1,2],N)
for i, v in zip(ind,values):
    strip_08[:,i:] = v
strip_08_trans = strip_08.T


# for 16 strips
N = 16
strip_16 = np.copy(arr_base)
ind = np.arange(0,Nx,Nx//N)
values = np.resize([1,2],N)
for i, v in zip(ind,values):
    strip_16[:,i:] = v
strip_16_trans = strip_16.T


# for 32 strips
N = 32
strip_32 = np.copy(arr_base)
ind = np.arange(0,Nx,Nx//N)
values = np.resize([1,2],N)
for i, v in zip(ind,values):
    strip_32[:,i:] = v
strip_32_trans = strip_32.T

#%%

# save path for diagonals
sp_strip = os.path.join("array_text_files","ideal_patterns","strip_test")

# save all arrays
np.savetxt(os.path.join(sp_strip,"strip_02.txt"), strip_02)
np.savetxt(os.path.join(sp_strip,"strip_04.txt"), strip_04)
np.savetxt(os.path.join(sp_strip,"strip_08.txt"), strip_08)
np.savetxt(os.path.join(sp_strip,"strip_16.txt"), strip_16)
np.savetxt(os.path.join(sp_strip,"strip_32.txt"), strip_32)
np.savetxt(os.path.join(sp_strip,"strip_02_trans.txt"), strip_02_trans)
np.savetxt(os.path.join(sp_strip,"strip_04_trans.txt"), strip_04_trans)
np.savetxt(os.path.join(sp_strip,"strip_08_trans.txt"), strip_08_trans)
np.savetxt(os.path.join(sp_strip,"strip_16_trans.txt"), strip_16_trans)
np.savetxt(os.path.join(sp_strip,"strip_32_trans.txt"), strip_32_trans)

#%% graphic of new patterns 

# view all four figures
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
plt.show()

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
plt.show()

