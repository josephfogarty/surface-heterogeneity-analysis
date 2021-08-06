"""
A code to calculate ice fraction
and save as csv
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

# reset matplotlib to defalt settings
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)



# define constants - these are changed in class cnst in constants.py
root = cnst.root
ice = float(cnst.ice_temp)
water = float(cnst.water_temp)

# clear all plots
plt.close('all')

# filename for surfaces
fn = 'SIPS200' # filename for surfaces
# where to load the data from
lp_surfaces = os.path.join(root, 'surfaces', 'SIPS200_templates','no_ponds')
# where to save the results
sp_csv = os.path.join(root, 'results','ice_fraction_txts',fn)

# to become a dataframe
ice_frac_list = []


# load surfaces, get ice fraction, and put into pandas dataframe
for filename in os.listdir(lp_surfaces):

    # iterate through surfaces
    if filename.endswith(".txt") or filename.endswith(".gz"):

        # load array
        arr = np.loadtxt(os.path.join(lp_surfaces,filename))

        # empty dict for storing data
        ice_stat = {}

        # print
        print(f'\n  Analyzing: {filename}')

        # calculate ice fraction statistics
        ice_stat['sfc'] = filename[:-3]
        ice_stat['arr_size'] = np.size(arr)
        ice_stat['arr_shape'] = np.shape(arr)

        # unique element statistics
        unique, counts = np.unique(arr, return_counts=True)
        for uv, count in zip(unique, counts):
            ice_stat[str(uv)+' count'] = count

        # append to list
        ice_frac_list.append(ice_stat)

# convert to pandas df
ice_frac_df = pd.DataFrame(ice_frac_list)

# calculate percentages and ratios
# for ice fraction df, calculate percentages and ratios
ice_frac_df['ice_percent'] = ice_frac_df['100.0 count']/ice_frac_df['arr_size']*100
ice_frac_df['water_percent'] = ice_frac_df['200.0 count']/ice_frac_df['arr_size']*100
ice_frac_df['ice_to_water_ratio'] = ice_frac_df['ice_percent']/ice_frac_df['water_percent']
ice_frac_df['water_to_ice_ratio'] = ice_frac_df['water_percent']/ice_frac_df['ice_percent']

# sort and write to csv
ice_frac_df = ice_frac_df.sort_values('sfc')
ice_frac_df.to_csv(os.path.join(sp_csv,'ice_fraction_stats.csv'))

# create bar chart of ice fractions
barlabels = list(ice_frac_df['sfc'])
x = np.arange(len(barlabels))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x-width/2, ice_frac_df['water_percent'], width, label = 'Water')
rects2 = ax.bar(x+width/2, ice_frac_df['ice_percent'], width, label = 'Ice')
ax.set_ylabel('Percent (%)')
ax.set_title('Ice Fraction of Different Surfaces')
ax.set_xticks(x)
ax.axhline(y=0,xmin=0,color='k')
ax.set_xticklabels(barlabels,rotation=45)
ax.legend()
plt.tight_layout()
plt.show()
plt.savefig(os.path.join(sp_csv,'bar_graph.png'))
