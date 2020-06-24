"""
A code to quantify surface heterogeneity
using length between transitions
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os
import json
from scipy.stats import kurtosis
from scipy.stats import skew

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

# load the transition length data                 
patterns = ['beaufo_2000_aug31', 'cafram_2000_aug07', 'esiber_2000_jul06']

# bar graph properties (for later)
width = 0.35
labels = ['beaufo', 'cafram', 'esiber']
map_comps = 'BCE'
sp = os.path.join(root, 'results','transition_scale_sk_barplots')
x = np.arange(len(labels))  # the label locations

# initialize dictionaries
skew_dict_all = {}
kurt_dict_all = {}
skew_dict_x = {}
kurt_dict_x = {}
skew_dict_y = {}
kurt_dict_y = {}
skew_dict_water = {}
kurt_dict_water = {}
skew_dict_ice = {}
kurt_dict_ice = {}

# load data and calculate statistics
for pattern in patterns:
    
    # base load path
    lp = os.path.join(root, 'results','transition_scale_txts')
    
    # get two filenames for x and y
    filename_x = pattern + '_transcales_x.txt'
    filename_y = pattern + '_transcales_y.txt'
    
    # load both as separate dictionaries
    transtats_x = json.load(open(os.path.join(lp,filename_x)))
    transtats_y = json.load(open(os.path.join(lp,filename_y)))
    
    # get different groups of transition lengths 
    all_transition_lengths = transtats_x[str(ice)] + transtats_x[str(water)] \
                           + transtats_y[str(ice)]  + transtats_y[str(water)]
    transition_lengths_x = transtats_x[str(ice)] + transtats_x[str(water)]
    transition_lengths_y = transtats_y[str(ice)] + transtats_y[str(water)]
    transition_lengths_water = transtats_x[str(ice)] + transtats_y[str(ice)]
    transition_lengths_ice = transtats_x[str(water)] + transtats_y[str(water)]
      
    # calculate skewness/kurtosis for ALL and append
    skew_dict_all[pattern+'_all'] = skew(all_transition_lengths)
    kurt_dict_all[pattern+'_all'] = kurtosis(all_transition_lengths)
    
    # calculate skewness/kurtosis for x direction and append
    skew_dict_x[pattern+'_x'] = skew(transition_lengths_x)
    kurt_dict_x[pattern+'_x'] = kurtosis(transition_lengths_x)
    
    # calculate skewness/kurtosis for y direction and append
    skew_dict_y[pattern+'_y'] = skew(transition_lengths_y)
    kurt_dict_y[pattern+'_y'] = kurtosis(transition_lengths_y)
    
    # calculate skewness/kurtosis for water lengths and append
    skew_dict_water[pattern+'_water'] = skew(transition_lengths_water)
    kurt_dict_water[pattern+'_water'] = kurtosis(transition_lengths_water)
    
    # calculate skewness/kurtosis for ice lengths and append
    skew_dict_ice[pattern+'_ice'] = skew(transition_lengths_ice)
    kurt_dict_ice[pattern+'_ice'] = kurtosis(transition_lengths_ice)

#### Now plot some bar graphs ####

# plot skewness for ALL and save
fig, ax = plt.subplots()
ax.bar(labels, list(skew_dict_all.values()), width)
ax.set_ylabel('Skewness')
ax.set_title('Skewness of All Ice/Water Transition Lengths')
ax.set_xticklabels(labels)
plt.savefig(os.path.join(sp,map_comps+'_skewness.png'))

# plot kurtosis for ALL and save
fig, ax = plt.subplots()
ax.bar(labels, list(kurt_dict_all.values()), width)
ax.set_ylabel('Kurtosis')
ax.set_title('Kurtosis of All Ice/Water Transition Lengths')
ax.set_xticklabels(labels)
plt.savefig(os.path.join(sp,map_comps+'_kurtosis.png'))

# plot skewness for x/y comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, list(skew_dict_x.values()), width, label=r'$x$')
rects2 = ax.bar(x + width/2, list(skew_dict_y.values()), width, label=r'$y$')
ax.set_ylabel('Skewness')
ax.set_title('Comparison of Transition Length Skewness between $x$ and $y$')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig(os.path.join(sp,map_comps+'_skewness_comp_xy.png'))

# plot kurtosis for x/y comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, list(kurt_dict_x.values()), width, label=r'$x$')
rects2 = ax.bar(x + width/2, list(kurt_dict_y.values()), width, label=r'$y$')
ax.set_ylabel('Skewness')
ax.set_title('Comparison of Transition Length Kurtosis between $x$ and $y$')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig(os.path.join(sp,map_comps+'_kurtosis_comp_xy.png'))

# plot skewness for ice/water comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, list(skew_dict_water.values()), width, label='Water')
rects2 = ax.bar(x + width/2, list(skew_dict_ice.values()), width, label='Ice')
ax.set_ylabel('Skewness')
ax.set_title('Comparison of Transition Length Skewness between Ice and Water')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig(os.path.join(sp,map_comps+'_skewness_comp_icewater.png'))

# plot kurtosis for ice/water comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, list(kurt_dict_water.values()), width, label='Water')
rects2 = ax.bar(x + width/2, list(kurt_dict_ice.values()), width, label='Ice')
ax.set_ylabel('Kurtosis')
ax.set_title('Comparison of Transition Length Kurtosis between Ice and Water')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig(os.path.join(sp,map_comps+'_kurtosis_comp_icewater.png'))


### PDF of transition lengths ###
#### need to rework this section ####


## PDF using a Gaussian kernel of both water and ice transitions in x and y
#arr_total = pd.Series(tsx_list[arr][ice] + tsx_list[arr][water]
#                    + tsy_list[arr][ice] + tsy_list[arr][water])
#arr_total.plot.density(label=f"{pattern}",legend='best')
#plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_{pattern}_all_pdf.png'))
#plt.close()
#
## PDF using a Gaussian kernel of only ice transitions in x and y
#arr_total = pd.Series(tsx_list[arr][ice] + tsy_list[arr][ice])
#arr_total.plot.density(label=f"{patterns[arr]}",legend='best')
#plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_{pattern}_ice_pdf.png'))
#plt.close()
#
## PDF using a Gaussian kernel of only water transitions in x and y
#arr_total = pd.Series(tsx_list[arr][water] + tsy_list[arr][water])
#arr_total.plot.density(label=f"{patterns[arr]}",legend='best')
#plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_{pattern}_water_pdf.png'))
#plt.close()
#
#for i in range(len(tsx_list)):
#    arr_total = tsx_list[i][ice]+tsx_list[i][water] + tsy_list[i][ice] + tsy_list[i][water]
#    # histrogram using raw data
#    # fixed bin size
#    bins = np.arange(0, 100, 5) # fixed bin size
#    plt.hist(arr_total, bins=bins, alpha=0.5)
#    plt.title('Histogram for Transition Lengths (fixed bin size)')
#    plt.xlabel('Length (bin size = 5)')
#    plt.ylabel('Count')
#    plt.savefig(os.path.join(root,'results','transition_pdfs',f'{patterns[i]}_hist.png'))
#    plt.close()




















