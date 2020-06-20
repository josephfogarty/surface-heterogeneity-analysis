"""
A code to quantify surface heterogeneity
using length between transitions
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os

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

# clear all plots
plt.close('all')

##### create semivariograms to compare #####

# load the array text file from the surface folder
# current options: checkerboard, strips
#                 beaufo_2000_aug31, esiber_2000_jul06
#                 cafram_2000_aug07
pattern = 'beaufo_2000_aug31'
peak = False
#lp = os.path.join(root, 'surfaces',pattern,'arrays'); s_cutoff = -17
#lp = os.path.join(root,'surfaces',pattern,'arrays','perp'); s_cutoff = -22
lp = os.path.join(root, 'surfaces',pattern,'arrays'); s_cutoff = -4
#checkerboard=-17, strips=-22


################# all options should be able to be set above #################

# set strings used to save variables from parameters set above
# titlestring
# set filename for saving
fname = f'{pattern}'
struc_title = f"Structure Functions - {pattern}"
int_scale_title = f'Integral Het. Scale - {pattern}'
print(f"\n  Title to be used: {struc_title}")
print(f"  Filename to be used: {fname}")


# iterate over files
arr = np.loadtxt(os.path.join(lp,'T_s_remote_ice.txt'))
print(f"\n  Importing from {os.path.join(lp,'T_s_remote_ice.txt')}")

a = np.array([[0,0,1,1,1,1,1],
             [0,2,0,0,1,1,1],
             [0,2,0,0,1,1,1],
             [0,2,1,1,1,0,0],
             [0,3,2,2,0,2,1]])

for row in arr:
    d = np.diff(row) != 0
    idx = np.concatenate(([0], np.flatnonzero(d) + 1))
    c = np.diff(np.concatenate((idx, [len(row)])))
    print(len(c))
    print('v', row[idx])
    print('c', c)













