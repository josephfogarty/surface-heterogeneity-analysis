"""
A code to quantify surface heterogeneity
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os

# load the array text file
lp_theta = os.path.join("LES_ready","gridtest","beaufo_2000aug31a_3c_192","T_s_remote_ice.txt")
lp_rough = os.path.join("LES_ready","gridtest","beaufo_2000aug31a_3c_192","zo_remote_ice.txt")
arr_theta = np.loadtxt(lp_theta)
arr_rough = np.loadtxt(lp_rough)

#%% semivariogram

def semivariogram(arr):
    
    # range of rx
    rx_vals = np.arange(np.shape(arr)[1])
    
    semivar = []
    
    # spatial translation vector
    for rx in rx_vals:
        
        # list for all rows - to be averaged
        avg_of_rows = []
        
        # for each row in the array
        for row in range(np.shape(arr)[0]):
            
            # create list of values
            avg_of_cols = []
            
            # for each column
            for col in range(np.shape(arr)[0]-rx):
                
                # calculate squared difference
                sq_diff = (arr[row,col] - arr[row,col+rx])**2.0
                
                # add to list
                avg_of_cols.append(sq_diff)
            
            # calculate mean of row
            row_avg = np.mean(avg_of_cols)
            
            # add to list
            avg_of_rows.append(row_avg)
        
        # get the structure function for this translation vector
        avg_of_rx = np.mean(avg_of_rows)
        
        # add to list
        semivar.append(avg_of_rx)
    
    return rx_vals, np.array(semivar)

#%% calculation semivariogram

# using my method
rx_rough, semivar_rough = semivariogram(arr_rough)
rx_theta, semivar_theta = semivariogram(arr_theta)
#semivar_theta/semivar_rough

# using scikit-gstat
from skgstat import Variogram
# random coordinates
coords = np.random.randint(0, np.shape(arr_theta)[0], (150,2))
values = np.fromiter((arr_theta[c[0], c[1]] for c in coords), float)
V = Variogram(coords,values)
V.plot()
V.distance_difference_plot()


#%%






#%% plotting

fig, ax = plt.subplots()
ax.plot(rx_theta,semivar_theta,label=r"$D_{\theta\theta}$")





















