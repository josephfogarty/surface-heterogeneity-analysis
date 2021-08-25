# testing codes
# testing indices on an array
# then putting in the funcs_QH code

import numpy as np

arr1 = np.array([[1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]])

arr2 = np.array([[0,0,0,0,0,0],
                 [0,1,1,1,1,0],
                 [0,1,1,1,1,0],
                 [0,1,1,1,1,0],
                 [0,1,1,1,1,0],
                 [0,0,0,0,0,0]])

arr3 = np.array([[0,1,0,1,0,1],
                 [1,0,1,0,1,0],
                 [0,1,0,1,0,1],
                 [1,0,1,0,1,0],
                 [0,1,0,1,0,1],
                 [1,0,1,0,1,0]])

arr4 = np.array([[1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,0]])

surfaces = [arr1, arr2, arr3, arr4]



#%% contagion index

#%% moran's I

from libpysal.weights import lat2W
from esda.moran import Moran

for i in range(len(surfaces)):
    
    # surface
    Z = surfaces[i]

    # Create the matrix of weigthts
    w = lat2W(Z.shape[0], Z.shape[1])
    
    # Crate the pysal Moran object
    mi = Moran(Z, w) 
    
    # Verify Moran's I results
    print(f'\n  For surface {i}, MI = {mi.I:.2f}')
    print(f'  p_norm = {mi.p_norm:.3e}')



#%% evenness


# get information on patch types and frequency
pixel_stats = np.array(np.unique(arr1, return_counts=True)).T

# number of unique values
n = len(pixel_stats)

# sum of squared probabilities that each unique value ios randomly chosen
prob_sum = 0
for unique in pixel_stats:
    prob_sum += (unique[1]/np.size(arr1))**2.0

# calculate E
E = -1.0*np.log(prob_sum)/np.log(n)



def evenness(surface):
    
    # get information on patch types and frequency
    pixel_stats = np.array(np.unique(surface, return_counts=True)).T
    
    # number of unique values
    n = len(pixel_stats)
    
    # sum of squared probabilities that each unique value ios randomly chosen
    prob_sum = 0
    for unique in pixel_stats:
        prob_sum += (unique[1]/np.size(surface))**2.0
    
    # calculate E
    E = -100.0*np.log(prob_sum)/np.log(n)
    return E



for i in range(len(surfaces)):
    print(f'\n For array {i}, E = '+str(evenness(surfaces[i])))

