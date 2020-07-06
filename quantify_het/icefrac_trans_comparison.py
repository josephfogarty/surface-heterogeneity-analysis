"""
A code to compare transition length scales
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
lp_trans = os.path.join(root, 'results','scale_trans_comp',project)
lp_icefrac = os.path.join(root, 'results', 'ice_fraction_txts',project)
sp = os.path.join(root, 'results','fraction_trans_comp',project)

# load the ice fraction dataframe
ice_frac_df = pd.read_csv(os.path.join(lp_icefrac,'ice_fraction_stats.csv'),
                     usecols=['sfc','arr_size','arr_shape',
                              '100.0 count','200.0 count',
                              'ice_percent','water_percent',
                              'ice_to_water_ratio', 'water_to_ice_ratio'])

# load the transition scale dataframes
trans_df = pd.read_csv(os.path.join(lp_trans,'trans_length_statistics.csv'),
                     usecols=['sfc','mean','median','max','min',
                              'variance','skewness','kurtosis'])

# for transition lengths, create new dataframe to separate data and calculate ratios
trans_ice_list = list(trans_df[trans_df.sfc.str.contains('_ice',case=False)]['mean'])
trans_water_list = list(trans_df[trans_df.sfc.str.contains('_water',case=False)]['mean'])
trans_sfc_list = list(trans_df[trans_df.sfc.str.contains('_all',case=False)]['sfc'])
trans_sfc_list = [sfc[:-4] for sfc in trans_sfc_list]
# convert lists to list of dictionary
trans_temp_list = []
for s in range(len(trans_sfc_list)):
    tdict = {}
    tdict['sfc'] = trans_sfc_list[s]
    tdict['avg_ice_length'] = trans_ice_list[s]
    tdict['avg_water_length'] = trans_water_list[s]
    trans_temp_list.append(tdict)
trans_length_df = pd.DataFrame(trans_temp_list)
trans_length_df['ice_to_water_ratio'] = trans_length_df['avg_ice_length']/trans_length_df['avg_water_length']
trans_length_df['water_to_ice_ratio'] = trans_length_df['avg_water_length']/trans_length_df['avg_ice_length']


# choose what to compare
x = list(trans_length_df['ice_to_water_ratio'])
y = list(ice_frac_df['ice_to_water_ratio'])

fig, ax = plt.subplots()
ax.plot(x,y,'o')
ax.set_xlabel('$f_i/f_w$')
ax.set_ylabel('$l_i/l_w$')
ax.set_title('Correlation between Mean Transition Length Ratio and Ice Fraction')
lims = [
    np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
    np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
]

# now plot both limits against eachother
ax.plot(lims, lims, 'k--', alpha=0.75, zorder=0)
ax.set_aspect('equal')
ax.set_xlim(lims)
ax.set_ylim(lims)
plt.tight_layout()
plt.show()
plt.savefig(os.path.join(sp,'trans_frac_correlation.png'))