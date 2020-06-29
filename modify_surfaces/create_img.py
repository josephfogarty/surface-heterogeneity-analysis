"""
A code to display an array
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm

# reset matplotlib to defalt settings
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)

# import constants and funcs by going up one, importing, then going back down
os.chdir(os.path.join("D:",os.sep,"surface-heterogeneity-analysis"))
from constants import cnst
os.chdir(os.path.join("create_surfaces"))

# define constants - these are changed in class cnst in constants.py
root = cnst.root
ice_temp = cnst.ice_temp
water_temp = cnst.water_temp

# clear all plots
plt.close('all')

#colormap properties
cmap = ListedColormap(['xkcd:pale blue', 'xkcd:bright blue'])
bounds = [0, 150, 250]
norm = BoundaryNorm(bounds,cmap.N)

# load path for files
lp = os.path.join(root,'surfaces','SIPS10k_templates','no_ponds')
sp = os.path.join(root,'surfaces','SIPS10k_templates','no_ponds','img')

# for file in load path, create an image
for filename in os.listdir(lp):
    
    if filename.endswith(".gz"):
                
        # load the text file
        loaded_mat = np.loadtxt(os.path.join(lp,filename))
        
        # calculate counts of ice and water
        ic = np.count_nonzero(loaded_mat == ice_temp)
        wc = np.count_nonzero(loaded_mat == water_temp)
        l = np.size(loaded_mat)
        
        # print the filename
        print(f'\n  Imported {filename}')
        print(f'    with unique values {np.unique(loaded_mat)}')
        print(f'    with shape {np.shape(loaded_mat)}')
        print(f'    percentage of ice: {ic/l*100:.2f}%')
        print(f'    percentage of water: {wc/l*100:.2f}%')
        
        # plot as image
        fig = plt.figure(frameon=False,figsize=(5,5))
        ax = fig.add_axes([0,0,1,1])
        ax.axis('off')
        ax.imshow(loaded_mat,cmap=cmap,norm=norm)
        
        # save as image
        plt.savefig(os.path.join(sp,filename[:-3]+'.png'))
        
        # close
        plt.close()

