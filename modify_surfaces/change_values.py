"""
A code to change values in a surface
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

# reset matplotlib to defalt settings
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
reso = cnst.reso
conv = cnst.conv
ice = cnst.ice
water = cnst.water

# clear all plots
plt.close('all')

# import the file
# options: b2000aug31, e2001sep08, b2001sep03, c2000aug07, e2000jul06, e2000jul28
pattern = 'e2000jul28'
#lp = os.path.join(root, 'surfaces',pattern,'arrays'); s_cutoff = -17
#lp = os.path.join(root,'surfaces',pattern,'arrays','perp'); s_cutoff = -22
lp = os.path.join(root, 'surfaces',pattern+'.out'); s_cutoff = -4
#checkerboard=-17, strips=-22

# load the large arrays
arr = np.loadtxt(lp,delimiter=',')

# use this space for edits that need to be done
print(np.shape(arr))
print(np.unique(arr))
plt.matshow(arr)
plt.colorbar()
plt.show()



# save as the same file and 'overwrite' it
arr = np.savetxt(lp,arr)


