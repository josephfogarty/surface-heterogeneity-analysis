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



#%%
### finish plotting and save ###


# PDF using a Gaussian kernel of both water and ice transitions in x and y
arr_total = pd.Series(tsx_list[arr][ice] + tsx_list[arr][water]
                    + tsy_list[arr][ice] + tsy_list[arr][water])
arr_total.plot.density(label=f"{pattern}",legend='best')
plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_{pattern}_all_pdf.png'))
plt.close()

# PDF using a Gaussian kernel of only ice transitions in x and y
arr_total = pd.Series(tsx_list[arr][ice] + tsy_list[arr][ice])
arr_total.plot.density(label=f"{patterns[arr]}",legend='best')
plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_{pattern}_ice_pdf.png'))
plt.close()

# PDF using a Gaussian kernel of only water transitions in x and y
arr_total = pd.Series(tsx_list[arr][water] + tsy_list[arr][water])
arr_total.plot.density(label=f"{patterns[arr]}",legend='best')
plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_{pattern}_water_pdf.png'))
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




















