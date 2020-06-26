# constants for the sea ice solver

from os import path, sep

class cnst(object):

    ##### Constants #####

    # surface grid values
    label = 'theta'
    iceT = 270.15 # 266.15 # temp of ice, K
    waterT = 274.15 # temp of water, K
    iceR = 0.01 # roughness of ice, m
    waterR = 1.0 # roughness of water, m
    #label = 'rough'
    
    # template values
    ice_temp = 1
    water_temp = 2
    pond_temp = 3

    # spatial parameters
    Nx = 96 # number of grid cells in x direction
    Ny = 96 # number of grid cells in y direction
    reso = 96
    conv = 10000/reso

    # root path
    root = path.join("D:",sep,"surface-heterogeneity-analysis")
