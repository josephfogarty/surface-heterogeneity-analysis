"""
A code to change values in a surface
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
iceT = cnst.iceT
waterT = cnst.waterT
iceR = cnst.waterR
waterR = cnst.waterR
icetemp = cnst.ice_temp
watertemp = cnst.water_temp
pondtemp = cnst.pond_temp

# clear all plots
plt.close('all')

# import the file
# need to edit: e2000jul28
# completed: b2000aug31,e2001sep08,b2001sep03,c2000aug07,e2000jul06
patterns = ['b2000aug31','e2001sep08','b2001sep03',
            'c2000aug07','e2000jul06','e2000jul28']

# choose pattern, and load array
pattern = patterns[1]
lp = os.path.join(root, 'surfaces',pattern+'.out')
arr = np.loadtxt(lp)
    
# print unique values, sixe, and show array
print(f'\n  Unique values: {np.unique(arr)}')
print(f'  Shape of array: {np.shape(arr)}')
plt.matshow(arr)
plt.show()

#%%

# set ice, water, pond values
ice_val = 7
water_val = 6
pond_val = 1
fname = f'{pattern}.gz'

# reassign - template with ponds
arr_temp_ponds = np.copy(arr)
arr_temp_ponds[arr_temp_ponds == ice_val] = icetemp
arr_temp_ponds[arr_temp_ponds == water_val] = watertemp
arr_temp_ponds[arr_temp_ponds == pond_val] = pondtemp
np.savetxt(os.path.join(root,'surfaces','SIPS10k_templates','ponds',fname),arr_temp_ponds)

# reassign - template with no ponds
arr_temp = np.copy(arr)
arr_temp[arr_temp == ice_val] = icetemp
arr_temp[arr_temp == water_val] = watertemp
arr_temp[arr_temp == pond_val] = icetemp
np.savetxt(os.path.join(root,'surfaces','SIPS10k_templates','no_ponds',fname),arr_temp)


## reassign - temperature where ponds = ice
#arr_T = np.copy(arr)
#arr_T[arr_T == ice_val] = iceT
#arr_T[arr_T == water_val] = waterT
#arr_T[arr_T == pond_val] = iceT
#np.savetxt(os.path.join(root,'surfaces','SIPS10k_values','temp',fname),arr)
#
## reassign - roughness where ponds = ice
#arr_R = np.copy(arr)
#arr_R[arr_R == ice_val] = iceR
#arr_R[arr_R == water_val] = waterR
#arr_R[arr_R == pond_val] = iceR
#np.savetxt(os.path.join(root,'surfaces','SIPS10k_values','rough',fname),arr)






