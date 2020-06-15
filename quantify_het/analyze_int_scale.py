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

df_maps = df.loc[df['pattern'] == 'T_s_remote_ice']




















