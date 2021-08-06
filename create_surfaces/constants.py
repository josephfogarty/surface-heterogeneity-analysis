# constants for the sea ice solver

from os import path, sep

class cnst(object):

    ##### Constants #####

    # surface grid values
    label = 'rough'
    iceT = 266.0 # 266.15 # temp of ice, K
    waterT = 274.0 # temp of water, K
    iceR = 0.01 # roughness of ice, m
    waterR = 0.001 # roughness of water, m
    #label = 'rough'
    
    # template values
    ice_temp = 100
    water_temp = 200
    pond_temp = 300

    # spatial parameters
    Nx = 100 #number of grid cells in x direction
    Ny = 100 # number of grid cells in y direction
    reso = 100
    conv = 10000/reso

    # root path
    root = path.join("D:",sep,"surface-heterogeneity-analysis")
