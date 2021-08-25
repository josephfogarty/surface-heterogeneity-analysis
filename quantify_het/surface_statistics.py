"""
Creating Surface Plots

A code to create a scatter plot of where different surfaces
would be placed if the x axis were ice fraction and the y axis were some
definition of heterogenetity
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import funcs_QH as fn

# folder with list of surfaces to analyze
root = os.path.join("D:",os.sep,"surface-heterogeneity-analysis")
lp_all = os.path.join(root, 'surfaces', 'quantitative_lattice')

# dataframe to store surface statistic information
df = pd.DataFrame(columns = ['surface', 'ice_frac', 'water_frac', 'int_length',
                             'trans_length', 'evenness', 'moran_i_rook',
                             'moran_i_queen'])
  
#%%
  
# iterate through all surfaces we want
for surface_file in os.listdir(lp_all):
    
    # condition: only the low resolution surfaces with no pond
    if surface_file.endswith("nopond_lowres.gz"):
        
        print('\n  Analyzing '+surface_file)
        
        # load the surface as an array
        surface = np.loadtxt(os.path.join(lp_all, surface_file))
        
        # ice fraction, for the x-axis
        ice_frac_dict = fn.ice_fraction(surface)
        ice_frac = ice_frac_dict['100.0 count']/ice_frac_dict['total count']
        water_frac = ice_frac_dict['200.0 count']/ice_frac_dict['total count']
        
        # semivariogram
        rx_vals, semivar, l_p = fn.semivariogram(surface)
        
        # transition_length
        all_length_information = fn.calculate_transition_statistics(surface)
        avg_ice_length = np.mean(all_length_information[100.0])
        avg_water_length = np.mean(all_length_information[200.0])
        avg_patch_length = (avg_ice_length + avg_water_length)/2.0
        
        # evenness
        evenness = fn.evenness(surface)
        
        # moran
        rook, queen = fn.moran(surface)
        moran_i_rook = rook[0]
        moran_i_queen = queen[0]
        
        df = df.append({'surface' : surface_file,
                        'ice_frac' : ice_frac,
                        'water_frac' : water_frac,
                        'int_length' : l_p,
                        'trans_length' : avg_patch_length,
                        'evenness' : evenness,
                        'moran_i_rook' : moran_i_rook,
                        'moran_i_queen' : moran_i_queen},
                        ignore_index = True)


#%% create a plot for the surfaces

# first show the surfaces with their name

# save path
sp_all_im = os.path.join(root,'results','figures')

# statistics
stat_fmt = ['','','',
            ('Integral Length Scale', r'$L_p$'),
            ('Transition Length Scale', r'$L_{tr}$'),
            ('Evenness', r'$E$'),
            ('Moran\'s I (Rook)', r'$I_{rook}$'),
            ('Moran\'s I (Queen)', r'$I_{queen}$')]

# now create a plot for each statistic in the df to compare to ice fraction
for i in range(3,len(df.columns)):
    
    # statistic to plot against ice fraction
    stat = df.columns[i]
    stat_full_name = stat_fmt[i][0]
    stat_mathtype = stat_fmt[i][1]
    
    # create figure
    plt.rcParams.update({'font.size': 14})
    fig, ax = plt.subplots(figsize=(7,5))
    
    # plot individually each point and label
    for index, row in df.iterrows():
        ax.scatter(row['ice_frac'], row[stat], label=row['surface'][:-17])
    
    # rest of the plot
    ax.set_ylabel(stat_mathtype)
    ax.set_xlabel('Ice Fraction')
    ax.set_title(f'Ice Fraction vs. {stat_full_name}')
    #plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
    #plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
    plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)
    ax.axvline(x=0,ymin=0,color='k')
    ax.axhline(y=0,xmin=0,color='k')
    plt.rcParams.update({'font.size': 12})
    ax.legend(bbox_to_anchor=(1.04,1),loc="upper left")
    plt.tight_layout()
    fig.savefig(os.path.join(sp_all_im,'fi_vs_'+stat+'.png'))
    plt.close('all')
        
        
        
        