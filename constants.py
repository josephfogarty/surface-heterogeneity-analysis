# constants for the sea ice solver

from os import path, sep

class cnst(object):

    ##### Constants #####

    # surface grid values
    label = 'theta'
    ice = 270.15 # 266.15 # temp of ice, K
    water = 274.15 # temp of water, K
    #ice = 0.01 # roughness of ice, m
    #water = 1.0 # roughness of water, m
    #label = 'rough'

    # spatial parameters
    Nx = 96 # number of grid cells in x direction
    Ny = 96 # number of grid cells in y direction
    reso = 96
    conv = 10000/reso

    # root path
    root = path.join("D:",sep,"surface-heterogeneity-analysis")
