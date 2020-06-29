"""
A code to compare int_het length scales and transition length scales
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
lp = os.path.join(root, 'results','scale_trans_comp',project)
sp = os.path.join(root, 'results','scale_trans_comp',project)

# load both dataframes
int_df = pd.read_csv(os.path.join(lp,'int_het_scale_statistics.csv'),
                     usecols=['pattern','lp','filename'])
trans_df = pd.read_csv(os.path.join(lp,'trans_length_statistics.csv'),
                     usecols=['sfc','mean','median','max','min',
                              'variance','skewness','kurtosis'])

# for int_df, average the x and y values to get 6 average length values
int_het_scale_x = list(int_df[int_df.filename.str.contains('_x',case=False)]['lp'])
int_het_scale_y = list(int_df[int_df.filename.str.contains('_y',case=False)]['lp'])
sfc_x = list(int_df[int_df.filename.str.contains('_x',case=False)]['pattern'])
sfc_y = list(int_df[int_df.filename.str.contains('_y',case=False)]['pattern'])
if sfc_x == sfc_y: # make sure the patterns are equal
    int_df = pd.DataFrame(
            {'sfc': sfc_x,
             'lp_x': int_het_scale_x,
             'lp_y': int_het_scale_y            
             })
int_df['lp_avg'] = int_df.mean(axis=1)
int_df.set_index('sfc')

# choose what to compare
x = list(int_df['lp_avg'])
y = list(list(trans_df[trans_df.sfc.str.contains('_all',case=False)]['kurtosis']))
corr = 'Kurtosis'
sfc = 'All'

fig, ax = plt.subplots()
ax.plot(x,y,'o')
ax.set_xlabel('Integral Length Scale, $L_p$')
ax.set_ylabel(corr+' of Transition Lengths')
ax.set_title(corr+' Correlation to '+sfc+' $L_p$')
plt.tight_layout()
plt.savefig(os.path.join(sp,corr+'_'+sfc+'_correlation.png'))