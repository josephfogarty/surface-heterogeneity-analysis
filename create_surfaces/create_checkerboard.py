# code to create a heterogeneous surface

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import os

# add to python path
import sys
sys.path.insert(1, os.path.join('D:',os.sep,'surface-heterogeneity-analysis'))
from constants import cnst
import funcs as fn

# Colormap properties for ice, water, and pond
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
cmap = ListedColormap(['black','xkcd:off white', 'xkcd:midnight blue', 'xkcd:cyan'])
bounds = [-0.4,0.5,1.5,2.5,3.5]
norm = BoundaryNorm(bounds,cmap.N)

# define constants - these are changed in class cnst in constants.py
Nx = cnst.Nx
Ny = cnst.Ny
ice = cnst.ice
water = cnst.water
root = cnst.root

# save paths for text and image files
sp = os.path.join(root,"surfaces","checkerboard","arrays")
sp_img = os.path.join(root,"surfaces","checkerboard","img")

#### create checkerboards ####

# create 2x2 checkerboard
checker2 = fn.conv_np_array_reso(np.array([[ice,water],[water,ice]]),Nx)

#
## create 4x4 checkerboard
#checker4 = np.array([[ice,water],[water,ice]])
#checker2 = fn.conv_np_array_reso(checker2,Nx)
#
## Create checkerboard 2x2 surface template
#surface1 = np.tile(np.concatenate((\
#          np.repeat(ice, int(Ny/2)),\
#          np.repeat(water, int(Ny/2)))),(int(Nx/2),1))
#surface2 = np.fliplr(surface1)
#surfacechecker2 = np.concatenate((surface1, surface2))
#
## Create checkerboard 4x4 surface template
#surface1 = np.tile(np.concatenate((\
#           np.repeat(ice, int(Ny/4)),\
#           np.repeat(water, int(Ny/4)))),(int(Nx/4),2))
#surface2 = np.fliplr(surface1)
#surfacechecker4 = np.concatenate((surface1, surface2, surface1, surface2))
#
## Create checkerboard 8x8 surface template
#surface1 = np.tile(np.concatenate((\
#          np.repeat(ice, int(Ny/8)),\
#          np.repeat(water, int(Ny/8)))),(int(Nx/8),4))
#surface2 = np.fliplr(surface1)
#surfacechecker8 = np.concatenate((surface1, surface2, surface1, surface2))
#surfacechecker8 = np.concatenate((surfacechecker8, surfacechecker8))

#### write arrays and images to a file ####
np.savetxt(os.path.join(sp,'checker2.txt'), checker2, delimiter=' ',fmt='%.2f')
#np.savetxt(os.path.join(sp,'checker4.txt'), surfacechecker4, delimiter=' ',fmt='%.2f')
#np.savetxt(os.path.join(sp,'checker8.txt'), surfacechecker8, delimiter=' ',fmt='%.2f')

