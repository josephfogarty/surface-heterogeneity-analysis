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
pattern = 'strip'
noise = True
reso = 96
#lp = os.path.join(root, 'surfaces','checkerboard','arrays'); s_cutoff = -17
lp = os.path.join(root,'surfaces','strips','arrays','perp'); s_cutoff = -22
#checkerboard=-17, strips=-22

################# all options should be able to be set above #################

# set strings used to save variables from parameters set above
# titlestring
if noise:
    nstring = [" noise","_noise"]
else:
    nstring = ["",""]
# set filename for saving
fname = f'{pattern}' + nstring[1]
struc_title = f"Structure Functions - {pattern}"+nstring[0]
int_scale_title = f'Integral Het. Scale - {pattern}'+nstring[0]
#print(f"\n  Title to be used: {struc_title}\n  Filename to be used: {fname}")

# create figure
fig_x, ax_x = plt.subplots(figsize=(10,6))
fig_y, ax_y = plt.subplots(figsize=(10,6))

# empty list for integral scale bar graph
int_scale_dict_x = {}
int_scale_dict_y = {}

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
            mean = 0
            stddev = 1
            arr = arr + np.random.normal(mean, stddev, np.shape(arr))
            #plt.matshow(arr)
            #plt.colorbar()
        
        # calculate rx and semivariogram, append int_scale
        rx, semivarx, int_scalex = fn.semivariogram(arr)
        ry, semivary, int_scaley = fn.semivariogram(arr.T)
        int_scale_dict_x[filename[:s_cutoff]] = int_scalex
        int_scale_dict_y[filename[:s_cutoff]] = int_scaley
        
        # create figure
        ax_x.plot(rx,semivarx/np.max(semivarx),label=f"{filename[:-17]}")
        ax_y.plot(ry,semivary/np.max(semivary),label=f"{filename[:-17]}")
        
        
# finish plotting and show

# formatting and labels
ax_x.set_xlabel(r'$r_x$',fontsize=20)
ax_x.set_ylabel(r'$D_{\theta\theta}/D_{\theta\theta,max}$',fontsize=20)
ax_x.tick_params(labelsize=16)
ax_x.legend(fontsize=16)
ax_x.set_title(struc_title+r", in $x$",fontsize=16)
fig_x.savefig(os.path.join(root,'results','structure_functions',fname + '_x.png'))

ax_y.set_xlabel(r'$r_y$',fontsize=20)
ax_y.set_ylabel(r'$D_{\theta\theta}/D_{\theta\theta,max}$',fontsize=20)
ax_y.tick_params(labelsize=16)
ax_y.legend(fontsize=16)
ax_y.set_title(struc_title+r", in $y$",fontsize=16)
fig_y.savefig(os.path.join(root,'results','structure_functions',fname+'_y.png'))


# bar graph of int length scales
width=0.35

fig, ax = plt.subplots(figsize=(9,6))
ax.bar(int_scale_dict_x.keys(), int_scale_dict_x.values(),width=width)
ax.set_title(int_scale_title+r" in $x$",fontsize=20)
ax.set_ylabel(r'$L_p$',fontsize=20)
ax.tick_params(labelsize=16)
plt.savefig(os.path.join(root,'results','int_het_scale_comparison',fname+'_x.png'))
plt.close()

fig, ax = plt.subplots(figsize=(9,6))
ax.bar(int_scale_dict_y.keys(), int_scale_dict_y.values(),width=width)
ax.set_title(int_scale_title+r" in $y$",fontsize=20)
ax.set_ylabel(r'$L_p$',fontsize=20)
ax.tick_params(labelsize=16)
plt.savefig(os.path.join(root,'results','int_het_scale_comparison',fname+'_y.png'))
plt.close()

##### using scikit-gstat #####

#from skgstat import Variogram
## random coordinates
#coords = np.random.randint(0, np.shape(arr)[0], (150,2))
#values = np.fromiter((arr[c[0], c[1]] for c in coords), float)
#V = Variogram(coords,values)
#V.plot()
#V.distance_difference_plot()



