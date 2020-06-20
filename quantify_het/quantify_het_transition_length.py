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
for filename in sorted(os.listdir(lp)):
    
    if filename.endswith(".txt"):
        
        # import array
        arr = np.loadtxt(os.path.join(lp,filename))
        print(f"\n  Importing {filename}")
        
        # change resolution of array - if needed
        if int(reso) != np.shape(arr)[0]:
            print(f"\n    Converting array from {np.shape(arr)} to reso={reso}")
            arr = fn.conv_np_array_reso(arr, int(reso))
        
        # calculate transition scales and lists

        
        
### finish plotting and save ###


### now save text files of int length scales ###

# columns should be same for both x and y
csv_columns = list(int_scale_dict_x.keys())

# csv filenames for both x and y
csv_x = fname + "_x.csv"
csv_y = fname + "_y.csv"

# save files for x
with open(os.path.join(root, 'results','int_het_scale_txts',csv_x), 'w') as f:
    for key, value in int_scale_dict_x.items():
        f.write('%s,%s\n' % (key, value))
f.close()
# and y
with open(os.path.join(root, 'results','int_het_scale_txts',csv_y), 'w') as f:
    for key, value in int_scale_dict_y.items():
        f.write('%s,%s\n' % (key, value))
f.close()












