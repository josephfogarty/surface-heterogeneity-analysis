# constants for the sea ice solver

from os import path, sep

class cnst(object):

    ##### Constants #####

    # surface grid values
    label = 'theta'
    ice = 270.15 # temp of ice, K
    water = 274.15 # temp of water, K
    #ice = 0.0002 # roughness of ice, m
    #water = 0.002 # roughness of water, m
    #label = 'rough'

    # spatial parameters
    Nx = 96 # number of grid cells in x direction
    Ny = 96 # number of grid cells in y direction

    # root path
    root = path.join("D:",sep,"surface-heterogeneity-analysis")
