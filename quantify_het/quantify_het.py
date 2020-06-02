"""
A code to quantify surface heterogeneity
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

# clear all plots
plt.close('all')

##### create semivariograms to compare #####

# load the array text file from the surface folder
# current options: checkerboard, strips
pattern = 'checkerboard'
noise = False
reso = 96
lp = os.path.join(root,"surfaces",pattern,"arrays")

# set strings used to save variables from parameters set above
# titlestring
if noise:
    nstring = [" (Noise)","_noise"]
else:
    nstring = ["",""]
# set filename for saving
fname = f'{pattern}' + nstring[1] + '.png'
titlestring = f"Structure Functions - {pattern}"+nstring[0]


# create figure
fig, ax = plt.subplots(figsize=(10,6))

# empty list for integral scale
int_scale_dict = {}

# iterate over files
for filename in sorted(os.listdir(lp)):
    
    if filename.endswith(".txt"):
        
        # import array
        arr = np.loadtxt(os.path.join(lp,filename))
        print(f"\n  Importing {filename}")
        
        # change resolution of array - if needed
        if int(reso) != np.shape(arr)[0]:
            print(f"\n    Converting array from {np.shape(arr)} to reso={reso}")
            arr = fn.conv_np_array_reso(arr, int(reso))
        
        
        # add noise to array, if flagged
        if noise:
            arr = arr + np.random.normal(0, 1, np.shape(arr))
        
        # calculate rx and semivariogram, append int_scale
        rx, semivar, int_scale = fn.semivariogram(arr)
        int_scale_dict[filename[:-17]] = int_scale
        
        # create figure
        ax.plot(rx,semivar/np.max(semivar),label=f"{filename[:-17]}")

# finish plotting and show

# formatting and labels
ax.set_xlabel(r'$r_x$',fontsize=20)
ax.set_ylabel(r'$D_{\theta\theta}/D_{\theta\theta,max}$',fontsize=20)
ax.tick_params(labelsize=16)
plt.legend(fontsize=16)
ax.set_title(titlestring,fontsize=16)
plt.savefig(os.path.join(root,'results','structure_functions',fname))

# bar graph of int length scales
fig, ax = plt.subplots(figsize=(9,6))
width=0.35
ax.bar(int_scale_dict.keys(), int_scale_dict.values(),width=width)
ax.set_title(f'Integral Het. Scale - {pattern}'+nstring[0],fontsize=20)
ax.set_ylabel(r'$L_p$',fontsize=20)
ax.tick_params(labelsize=16)
plt.savefig(os.path.join(root,'results','int_het_scale_comparison',fname))
plt.show()


##### using scikit-gstat #####

#from skgstat import Variogram
## random coordinates
#coords = np.random.randint(0, np.shape(arr)[0], (150,2))
#values = np.fromiter((arr[c[0], c[1]] for c in coords), float)
#V = Variogram(coords,values)
#V.plot()
#V.distance_difference_plot()



