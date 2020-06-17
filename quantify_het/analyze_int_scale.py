"""
A code to plot and compare integral heterogeneity length scales
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import glob

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
conv = cnst.conv

# clear all plots
plt.close('all')

#### obtain data ####

# create dataframe from all csvs in the load path
headers = ['pattern','lp']
lp = os.path.join(root,'results','int_het_scale_txts')

pd_list = []

# load in each pandas dataframe
for csv_file in os.listdir(lp):
    
    if csv_file.endswith('.csv'):
        
        # import filename
        print(f'\n  Importing {csv_file}')
        
        # read to pandas
        df = pd.read_csv(os.path.join(lp,csv_file),names=headers)
        
        # add filename column
        df['filename']=f'{csv_file[:-4]}'
        
        # add to df list
        pd_list.append(df)

# now concatenate
df = pd.concat(pd_list,ignore_index=True)        

#### analyze data ####

# get map data, for example
df_maps = df.loc[df['pattern'] == 'T_s_remote_ice']

# scale up
# in this case, to the 10km by 10km domain for SHEBA maps
df_maps['lp'] = conv*df_maps['lp']


# split into x and y
df_maps_x = df_maps[df_maps.filename.str.contains('_x',case=False)]
df_maps_y = df_maps[df_maps.filename.str.contains('_y',case=False)]


# plot total cooling
labels = ['beaufo', 'esiber', 'cafram']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots(figsize=(8,5))
rects1 = ax.bar(x + width/2, df_maps_x['lp'], width, label='x')
rects2 = ax.bar(x - width/2, df_maps_y['lp'], width, label='y')
ax.set_ylabel(r'$L_p$ (m)')
ax.set_title('Integral Length Scale of Different Maps')
ax.set_xticks(x)
#ax.axhline(y=0,xmin=0,color='k')
ax.set_xticklabels(labels)
ax.legend()

# save fig
sp = os.path.join(root,'results','int_het_scale_comparison','COMP_map.png')
fig.savefig(sp)






















