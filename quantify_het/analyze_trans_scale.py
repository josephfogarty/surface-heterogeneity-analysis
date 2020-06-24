"""
A code to quantify surface heterogeneity
using length between transitions
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os
import json
import pandas as pd
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

############################################################
######## all options should be able to be set above ########
############################################################

# initlaize pandas dataframe
df = pd.DataFrame(columns=['sfc','mean','median','max','min',
                           'variance','skewness','kurtosis'])

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
    all_lengths = transtats_x[str(ice)] + transtats_x[str(water)] \
                           + transtats_y[str(ice)]  + transtats_y[str(water)]
    x_lengths = transtats_x[str(ice)] + transtats_x[str(water)]
    y_lengths = transtats_y[str(ice)] + transtats_y[str(water)]
    water_lengths = transtats_x[str(ice)] + transtats_y[str(ice)]
    ice_lengths = transtats_x[str(water)] + transtats_y[str(water)]
    
    # create list to loop through
    trans_length_list = [(all_lengths, '_all'), 
                         (x_lengths,'_x'), 
                         (y_lengths, '_y'),
                         (water_lengths, '_water'),
                         (ice_lengths, '_ice')]
    
    # calculate statistics for different groups from above, and append
    for group in trans_length_list:
        df = df.append({'sfc':pattern+group[1],
                    'mean':np.mean(group[0]),
                    'median':np.median(group[0]),
                    'max':np.max(group[0]),
                    'min':np.min(group[0]),
                    'variance':np.var(group[0]),
                    'skewness':skew(group[0]),
                    'kurtosis':kurtosis(group[0])},
                    ignore_index=True)

# when finished, set 'surface' to be the index
df.set_index('sfc')

#### Now plot some bar graphs, using the pandas datafram above ####
#### You can sort each dataframe using strings such as '_x', '_ice', etc ####

# plot skewness for ALL and save
fig, ax = plt.subplots()
ax.bar(labels, list(df[df.sfc.str.contains('_all',case=False)]['skewness']),
       width)
ax.set_ylabel('Skewness')
ax.set_title('Skewness of All Ice/Water Transition Lengths')
ax.set_xticklabels(labels)
plt.savefig(os.path.join(sp,map_comps+'_skewness.png'))

# plot kurtosis for ALL and save
fig, ax = plt.subplots()
ax.bar(labels, list(df[df.sfc.str.contains('_all',case=False)]['kurtosis']),
       width)
ax.set_ylabel('Kurtosis')
ax.set_title('Kurtosis of All Ice/Water Transition Lengths')
ax.set_xticklabels(labels)
plt.savefig(os.path.join(sp,map_comps+'_kurtosis.png'))

# plot skewness for x/y comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_x',case=False)]['skewness']),
                width, label=r'$x$')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_y',case=False)]['skewness']),
                width, label=r'$y$')
ax.set_ylabel('Skewness')
ax.set_title('Comparison of Transition Length Skewness between $x$ and $y$')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig(os.path.join(sp,map_comps+'_skewness_comp_xy.png'))

# plot kurtosis for x/y comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_x',case=False)]['kurtosis']),
                width, label=r'$x$')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_y',case=False)]['kurtosis']),
                width, label=r'$y$')
ax.set_ylabel('Skewness')
ax.set_title('Comparison of Transition Length Kurtosis between $x$ and $y$')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig(os.path.join(sp,map_comps+'_kurtosis_comp_xy.png'))

# plot skewness for ice/water comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_water',case=False)]['skewness']),
                width, label='Water')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_ice',case=False)]['skewness']),
                width, label='Ice')
ax.set_ylabel('Skewness')
ax.set_title('Comparison of Transition Length Skewness between Ice and Water')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig(os.path.join(sp,map_comps+'_skewness_comp_icewater.png'))

# plot kurtosis for ice/water comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_water',case=False)]['kurtosis']),
                width, label='Water')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_ice',case=False)]['kurtosis']),
                width, label='Ice')
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




















