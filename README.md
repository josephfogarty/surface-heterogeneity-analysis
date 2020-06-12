# Surface Heterogeneity Analysis

This repo contains codes for creating, modifying, and quantifying surface heterogeneity.

## Structure

This sectiond details the structure of this repository. Outside of the following directories, the codes constants.py and funcs.py contain universal variables and functions used throughout the codes.

### Creating Surfaces

The folder `create_surfaces` contains two codes right now, one will create a checkerboard pattern of an array, and the other will create an array full of 'strips' - examples coming soon (they can also be seen in the `surfaces` folder)/

### Storing Surfaces

The folder `surfaces` organizes the different surfaces that are availabel to be analyzed, whether they are idealized patterns (such as strips or checkerboards) or real-world maps of water/ice (i.e. from SHEBA, see: https://nsidc.org/data/G02159).

### Modifying Surfaces

Currently, the the only function in the `modify_surfaces` folder is one that converts the resolution of an array to a different size (square resolutions only, for now). It does this by loading in the `funcs` module and upscaling if necessary and downscaling, using the mode of each individual cell block that is being downscaled. Pictures coming soon.

### Quantifying Heterogeneity

The only code in the folder `quantify_het` contains the code for quantifying the heterogeneity of a surface using semivariograms. For more details on this process, see the method outlined in Bou-Zeid et al. (2007, JAS) doi: https://doi.org/10.1175/JAS3826.1


### Results

All results from the `quantifying_het` folder will be stored here. This includes semivariograms, heterogeneity scales, and all comparisons between different patterns.



