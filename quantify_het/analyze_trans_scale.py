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
os.chdir(os.path.join("create_surfaces"))

# define constants - these are changed in class cnst in constants.py
label = cnst.label
root = cnst.root
reso = cnst.reso
conv = cnst.conv
ice = float(cnst.ice_temp)
water = float(cnst.water_temp)

# clear all plots
plt.close('all')

# parameters
project = 'SIPS200'
lp = os.path.join(root,'results','transition_scale_txts',project)
sp = os.path.join(root, 'results','trans_scale_barplots',project)
df_sp = os.path.join(root, 'results','scale_trans_comp',project)

# bar graph properties (for later)
width = 0.35
labels = ['b2000aug31', 'b2001sep03', 'c2000aug07',
          'e2000jul06', 'e2000jul28', 'e2001sep08']
map_comps = 'six_original'
x = np.arange(len(labels))  # the label locations

############################################################
######## all options should be able to be set above ########
############################################################

# initlaize pandas dataframe
df = pd.DataFrame(columns=['sfc','mean','median','max','min',
                           'variance','skewness','kurtosis'])

# iterate over files
for pattern in labels:
    
    print(f'\n  For {pattern}...')
    
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

# write the dataframe as a csv
df.to_csv(os.path.join(df_sp,'trans_length_statistics.csv'))
#%%
#### Now plot some bar graphs, using the pandas datafram above ####
#### You can sort each dataframe using strings such as '_x', '_ice', etc ####

# plot mean length for all and save
fig, ax = plt.subplots()
ax.bar(labels, list(df[df.sfc.str.contains('_all',case=False)]['mean']),
       width)
ax.set_ylabel('Mean')
ax.set_title('Mean of All Ice/Water Transition Lengths')
ax.set_xticklabels(labels,rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_mean.png'))

# plot mean length for x/y comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_x',case=False)]['mean']),
                width, label=r'$x$')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_y',case=False)]['mean']),
                width, label=r'$y$')
ax.set_ylabel('Mean')
ax.set_title('Comparison of Transition Length Mean between $x$ and $y$')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_mean_comp_xy.png'))

# plot mean length for ice/water comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_water',case=False)]['mean']),
                width, label='Water')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_ice',case=False)]['mean']),
                width, label='Ice')
ax.set_ylabel('Mean')
ax.set_title('Comparison of Transition Length Mean between Ice and Water')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_mean_comp_icewater.png'))






# plot median length for all and save
fig, ax = plt.subplots()
ax.bar(labels, list(df[df.sfc.str.contains('_all',case=False)]['median']),
       width)
ax.set_ylabel('Median')
ax.set_title('Median of All Ice/Water Transition Lengths')
ax.set_xticklabels(labels,rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_median.png'))

# plot mean length for x/y comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_x',case=False)]['median']),
                width, label=r'$x$')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_y',case=False)]['median']),
                width, label=r'$y$')
ax.set_ylabel('Median')
ax.set_title('Comparison of Transition Length Median between $x$ and $y$')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_median_comp_xy.png'))

# plot mean length for ice/water comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_water',case=False)]['median']),
                width, label='Water')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_ice',case=False)]['median']),
                width, label='Ice')
ax.set_ylabel('Median')
ax.set_title('Comparison of Transition Length Median between Ice and Water')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_median_comp_icewater.png'))







# plot variance length for all and save
fig, ax = plt.subplots()
ax.bar(labels, list(df[df.sfc.str.contains('_all',case=False)]['variance']),
       width)
ax.set_ylabel('Variance')
ax.set_title('Variance of All Ice/Water Transition Lengths')
ax.set_xticklabels(labels,rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_var.png'))

# plot variance length for x/y comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_x',case=False)]['variance']),
                width, label=r'$x$')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_y',case=False)]['variance']),
                width, label=r'$y$')
ax.set_ylabel('Variance')
ax.set_title('Comparison of Transition Length Variance between $x$ and $y$')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_var_comp_xy.png'))

# plot variance length for ice/water comparison and save
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,
                list(df[df.sfc.str.contains('_water',case=False)]['variance']),
                width, label='Water')
rects2 = ax.bar(x + width/2,
                list(df[df.sfc.str.contains('_ice',case=False)]['variance']),
                width, label='Ice')
ax.set_ylabel('Variance')
ax.set_title('Comparison of Transition Length Variance between Ice and Water')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_var_comp_icewater.png'))







# plot skewness for all and save
fig, ax = plt.subplots()
ax.bar(labels, list(df[df.sfc.str.contains('_all',case=False)]['skewness']),
       width)
ax.set_ylabel('Skewness')
ax.set_title('Skewness of All Ice/Water Transition Lengths')
ax.set_xticklabels(labels,rotation=45)
plt.savefig(os.path.join(sp,map_comps+'_skewness.png'))

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
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_skewness_comp_xy.png'))

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
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_skewness_comp_icewater.png'))







# plot kurtosis for ALL and save
fig, ax = plt.subplots()
ax.bar(labels, list(df[df.sfc.str.contains('_all',case=False)]['kurtosis']),
       width)
ax.set_ylabel('Kurtosis')
ax.set_title('Kurtosis of All Ice/Water Transition Lengths')
ax.set_xticklabels(labels,rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_kurtosis.png'))

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
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(sp,map_comps+'_kurtosis_comp_xy.png'))

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
ax.set_xticklabels(labels,rotation=45)
ax.legend()
plt.tight_layout()
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




















