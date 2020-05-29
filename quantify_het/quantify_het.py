"""
A code to quantify surface heterogeneity
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os

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


##### create semivariograms to compare #####


# load the array text file from the surface folder
lp = os.path.join(root,"surfaces","checkerboard","arrays")

# create figure
fig, ax = plt.subplots()

# iterate over files
for filename in os.listdir(lp):
    
    if filename.endswith(".txt"):
        
        # import array
        arr = np.loadtxt(os.path.join(lp,filename))
        print(f"importing {filename}")
        
        # change resolution of array
        arr = fn.conv_np_array_reso(arr, np.shape(arr)[0]*10)
        
        # add noise to array
        arr = arr + np.random.normal(0, 1, np.shape(arr))
        
        # calculate rx and semivariogram
        rx, semivar = fn.semivariogram(arr)
        
        # create figure
        ax.plot(rx,semivar/np.max(semivar),label=r"$D_{\theta\theta}$"+f" - {filename[:8]}")



plt.legend()
plt.show()


plt.imshow(arr)
plt.show()
##### calculation semivariogram #####

# using my method



## using scikit-gstat
#from skgstat import Variogram
## random coordinates
#coords = np.random.randint(0, np.shape(arr)[0], (150,2))
#values = np.fromiter((arr[c[0], c[1]] for c in coords), float)
#V = Variogram(coords,values)
#V.plot()
#V.distance_difference_plot()

















