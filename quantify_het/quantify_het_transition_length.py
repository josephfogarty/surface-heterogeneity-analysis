"""
A code to quantify surface heterogeneity
using length between transitions
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy import stats

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

##### create semivariograms to compare #####

# load the array text file from the surface folder
# current options: checkerboard, strips
#                 beaufo_2000_aug31, esiber_2000_jul06
#                 cafram_2000_aug07
pattern1 = 'beaufo_2000_aug31'
pattern2 = 'cafram_2000_aug07'
pattern3 = 'esiber_2000_jul06'
patterns = [pattern1, pattern2, pattern3]
#lp = os.path.join(root, 'surfaces',pattern,'arrays'); s_cutoff = -17
#lp = os.path.join(root,'surfaces',pattern,'arrays','perp'); s_cutoff = -22
lp1 = os.path.join(root, 'surfaces',pattern1,'arrays'); s_cutoff = -4
lp2 = os.path.join(root, 'surfaces',pattern2,'arrays'); s_cutoff = -4
lp3 = os.path.join(root, 'surfaces',pattern3,'arrays'); s_cutoff = -4
#checkerboard=-17, strips=-22


################# all options should be able to be set above #################

# set strings used to save variables from parameters set above
# titlestring
# set filename for saving
fname1 = f'{pattern1}_transition_pdf'
fname2 = f'{pattern2}_transition_pdf'
fname3 = f'{pattern3}_transition_pdf'
print(f"  Filename to be used: {fname1,fname2,fname3}")


# choose one map file
arr1 = np.loadtxt(os.path.join(lp1,'T_s_remote_ice.txt'))
arr2 = np.loadtxt(os.path.join(lp2,'T_s_remote_ice.txt'))
arr3 = np.loadtxt(os.path.join(lp3,'T_s_remote_ice.txt'))
print(f"\n  Importing from {os.path.join(lp1,'T_s_remote_ice.txt')}")
print(f"\n  Importing from {os.path.join(lp2,'T_s_remote_ice.txt')}")
print(f"\n  Importing from {os.path.join(lp3,'T_s_remote_ice.txt')}")

tsx_list = []
tsy_list = []

# change resolution of array - if needed
for arr in [arr1, arr2, arr3]:
    if int(reso) != np.shape(arr)[0]:
        print(f"\n    Converting array from {np.shape(arr)} to reso={reso}")
        arr = fn.conv_np_array_reso(arr, int(reso))
    
    # get transition statistics in x and y
    transtats_x = fn.calculate_transition_statistics(arr)
    tsx_list.append(transtats_x)
    transtats_y = fn.calculate_transition_statistics(arr.T)
    tsy_list.append(transtats_y)



### finish plotting and save ###

# tsx list sshould be same order as tsy list
for arr in range(len(tsx_list)):
    # PDF using a Gaussian kernel
    arr_total = pd.Series(tsx_list[arr][ice] + tsx_list[arr][water]
                        + tsy_list[arr][ice] + tsy_list[arr][water])
    arr_total.plot.density(label=f"{patterns[arr]}",legend='best')
plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_BCE_all_pdf.png'))
plt.close()

for arr in range(len(tsx_list)):
    # PDF using a Gaussian kernel
    arr_total = pd.Series(tsx_list[arr][ice] + tsy_list[arr][ice])
    arr_total.plot.density(label=f"{patterns[arr]}",legend='best')
plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_BCE_ice_pdf.png'))
plt.close()

for arr in range(len(tsx_list)):
    # PDF using a Gaussian kernel
    arr_total = pd.Series(tsx_list[arr][water] + tsy_list[arr][water])
    arr_total.plot.density(label=f"{patterns[arr]}",legend='best')
plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_BCE_water_pdf.png'))
plt.close()

for i in range(len(tsx_list)):
    arr_total = tsx_list[i][ice]+tsx_list[i][water] + tsy_list[i][ice] + tsy_list[i][water]
    # histrogram using raw data
    # fixed bin size
    bins = np.arange(0, 100, 5) # fixed bin size
    plt.hist(arr_total, bins=bins, alpha=0.5)
    plt.title('Histogram for Transition Lengths (fixed bin size)')
    plt.xlabel('Length (bin size = 5)')
    plt.ylabel('Count')
    plt.savefig(os.path.join(root,'results','transition_pdfs',f'{patterns[i]}_hist.png'))
    plt.close()




















