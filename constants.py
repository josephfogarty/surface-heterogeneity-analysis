# constants for the sea ice solver

from os import path, sep

class cnst(object):

    ##### Constants #####

    # surface grid values
    label = 'theta'
    iceT = 266.15 # 266.15 # temp of ice, K
    waterT = 274.15 # temp of water, K
    iceR = 0.01 # roughness of ice, m
    waterR = 1.0 # roughness of water, m
    #label = 'rough'
    
    # template values
    ice_temp = 100
    water_temp = 200
    pond_temp = 300

    # spatial parameters
    Nx = 96 # number of grid cells in x direction
    Ny = 96 # number of grid cells in y direction
    reso = 200
    conv = 10000/reso

    # root path
    root = path.join("D:",sep,"surface-heterogeneity-analysis")
