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
reso = 10000
conv = cnst.conv
ice_temp = cnst.ice_temp
water_temp = cnst.water_temp
iceT = cnst.iceT
waterT = cnst.waterT

# clear all plots
plt.close('all')

##### create semivariograms to compare #####

# load the array text file from the surface folder
# current options: checkerboard, strips, SIPS200, SIPS10k
project = 'SIPS10k'
noise = False
peak = False
lp = os.path.join(root, 'surfaces','SIPS10k_templates','no_ponds','to_analyze')
semivariogram_sp = os.path.join(root,'results','structure_functions',project)
int_bar_graph_sp = os.path.join(root,'results','int_het_scale_comparison',project)
int_scale_csv_sp = os.path.join(root, 'results','int_het_scale_txts',project)
s_cutoff = -3
#checkerboard=-17, strips=-22


################# all options should be able to be set above #################

# set strings used to save variables from parameters set above
# titlestring
if noise:
    nstring = [" noise","_noise"]
else:
    nstring = ["",""]

# empty dict for integral scale bar graph
int_scale_dict_x = {}
int_scale_dict_y = {}

# iterate over files
for filename in sorted(os.listdir(lp)):
    
    if filename.endswith(".gz"):
        
        # import array
        arr = np.loadtxt(os.path.join(lp,filename))
        print(f"\n  Importing {filename}")
        
        # assign the array with correct values
        arr[arr == ice_temp] = iceT
        arr[arr == water_temp] = waterT
        print(f'\n    Unique values after replacing template: {np.unique(arr)}')
        
        # set filename for saving
        fname = f'{filename[:s_cutoff]}'
        struc_title = f"Structure Functions - {fname}"
        int_scale_title = f'Integral Het. Scale - {fname}'
        
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
        rx, semivarx, int_scalex = fn.semivariogram(arr,peak=peak)
        ry, semivary, int_scaley = fn.semivariogram(arr.T,peak=peak)
        int_scale_dict_x[fname] = int_scalex
        int_scale_dict_y[fname] = int_scaley
        
        # create semivariogram in x
        fig_x, ax_x = plt.subplots(figsize=(10,6))
        ax_x.plot(rx,semivarx/np.max(semivarx),label=f"{fname}")
        ax_x.set_xlabel(r'$r_x$',fontsize=20)
        ax_x.set_ylabel(r'$D_{\theta\theta}/D_{\theta\theta,max}$',fontsize=20)
        ax_x.tick_params(labelsize=16)
        ax_x.legend(fontsize=16)
        ax_x.set_title(struc_title+r", in $x$",fontsize=16)
        fig_x.savefig(os.path.join(semivariogram_sp,fname + '_x.png'))
        
        # create semivariogram in y
        fig_y, ax_y = plt.subplots(figsize=(10,6))
        ax_y.plot(ry,semivary/np.max(semivary),label=f"{fname}")
        ax_y.set_xlabel(r'$r_y$',fontsize=20)
        ax_y.set_ylabel(r'$D_{\theta\theta}/D_{\theta\theta,max}$',fontsize=20)
        ax_y.tick_params(labelsize=16)
        ax_y.legend(fontsize=16)
        ax_y.set_title(struc_title+r", in $y$",fontsize=16)
        fig_y.savefig(os.path.join(semivariogram_sp,fname+'_y.png'))

        
### now save text files of int length scales ###

# csv filenames for both x and y
csv_x = project + "_x.csv"
csv_y = project + "_y.csv"

# save files for x
with open(os.path.join(int_scale_csv_sp,csv_x), 'w') as f:
    for key, value in int_scale_dict_x.items():
        f.write('%s,%s\n' % (key, value))
f.close()
# save files for y
with open(os.path.join(int_scale_csv_sp,csv_y), 'w') as f:
    for key, value in int_scale_dict_y.items():
        f.write('%s,%s\n' % (key, value))
f.close()

      
### save bar graph comparisons of int_het_scales ###

# bar graph parameters
width=0.35

# het scale in x
fig, ax = plt.subplots(figsize=(9,6))
ax.bar(int_scale_dict_x.keys(), int_scale_dict_x.values(),width=width)
ax.set_title(int_scale_title+r" in $x$",fontsize=20)
plt.xticks(rotation=45)
ax.set_ylabel(r'$L_p$',fontsize=20)
ax.tick_params(labelsize=16)
fig.tight_layout()
plt.savefig(os.path.join(int_bar_graph_sp,project+'_x.png'))
plt.close()

# het scale in y
fig, ax = plt.subplots(figsize=(9,6))
ax.bar(int_scale_dict_y.keys(), int_scale_dict_y.values(),width=width)
ax.set_title(int_scale_title+r" in $y$",fontsize=20)
plt.xticks(rotation=45)
ax.set_ylabel(r'$L_p$',fontsize=20)
ax.tick_params(labelsize=16)
fig.tight_layout()
plt.savefig(os.path.join(int_bar_graph_sp,project+'_y.png'))
plt.close()














