"""
A code to quantify surface heterogeneity
using length between transitions
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
trans_title = f"Transition Statistics - {pattern}"
print(f"\n  Title to be used: {trans_title}")
print(f"  Filename to be used: {fname}")


# choose one map file
arr = np.loadtxt(os.path.join(lp,'T_s_remote_ice.txt'))
print(f"\n  Importing from {os.path.join(lp,'T_s_remote_ice.txt')}")

# change resolution of array - if needed
if int(reso) != np.shape(arr)[0]:
    print(f"\n    Converting array from {np.shape(arr)} to reso={reso}")
    arr = fn.conv_np_array_reso(arr, int(reso))

# get transition statistics in x and y
transtats_x = fn.calculate_transition_statistics(arr)
transtats_y = fn.calculate_transition_statistics(arr.T)







        
        
### finish plotting and save ###

#s = pd.Series(row_data_list)
#ax = s.plot.density(label="KDE for Heterogeneity Lengths",legend=('best'),x=r"$Length$")
#
#
## Show the plots
#plt.show()














