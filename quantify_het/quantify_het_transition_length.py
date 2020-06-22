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

# Look for interval changes and pad with bool 1s on either sides to set the
# first interval for each row and for setting boundary wrt the next row
p = np.ones((len(arr),1), dtype=bool)
m = np.hstack((p, arr[:,:-1]!=arr[:,1:], p))

# Look for interval change indices in flattened array version
intv = m.sum(1).cumsum()-1

# Get index and counts
idx = np.diff(np.flatnonzero(m.ravel()))  
count = np.delete(idx, intv[:-1])
val = arr[m[:,:-1]]

# Get couples and setup offsetted interval change indices
grps = np.c_[val,count]
intvo = np.r_[0,intv-np.arange(len(intv))]

# Finally slice and get output for each row
out = [grps[i:j] for (i,j) in zip(intvo[:-1], intvo[1:])]

# obtain number of transitions and each transition length per row
#for row in len(range(out)):
#    print(row)








## iterate over files
#for filename in sorted(os.listdir(lp)):
#    
#    if filename.endswith(".txt"):
#        
#        # import array
#        arr = np.loadtxt(os.path.join(lp,filename))
#        print(f"\n  Importing {filename}")
#        
#        # change resolution of array - if needed
#        if int(reso) != np.shape(arr)[0]:
#            print(f"\n    Converting array from {np.shape(arr)} to reso={reso}")
#            arr = fn.conv_np_array_reso(arr, int(reso))
        
        # calculate transition scales and lists

        
        
### finish plotting and save ###














