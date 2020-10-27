# getting some plots

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

plt.close('all')

# load in csv
df = pd.read_csv('test.csv')


# choose what to compare
x1 = list(df['iw_ratio'])
y1 = list(df['trans_ratio'])
x2 = list(df['iw_ratio'])
y2 = list(df['med_trans_ratio'])
x3 = list(df['iw_ratio'])
y3 = list(df['var_iw_ratio'])
x4 = list(df['iw_ratio'])
y4 = list(df['avg_int_het_scale'])

fig, ax = plt.subplots(2,2,figsize=(8,8))
plt.rcParams.update({'font.size': 14})
ax[0,0].plot(x1,y1,'ko')
ax[0,0].set_xlabel('$f_i/f_w$')
ax[0,0].set_ylabel('avg($l_i$)/avg$(l_w)$')
ax[0,0].set_title('Ice-to-Water Ratio vs. \n Mean Transition Length Ratio')
lims = [
    np.min([ax[0,0].get_xlim(), ax[0,0].get_ylim()]),  # min of both axes
    np.max([ax[0,0].get_xlim(), ax[0,0].get_ylim()]),  # max of both axes
]
ax[0,0].plot(lims, lims, 'k--', alpha=0.75, zorder=0)
ax[0,0].set_aspect('equal')
ax[0,0].set_xlim(lims)
ax[0,0].set_ylim(lims)

ax[0,1].plot(x2,y2,'ko')
ax[0,1].set_xlabel('$f_i/f_w$')
ax[0,1].set_ylabel('med($l_i$)/med$(l_w)$')
ax[0,1].set_title('Ice-to-Water Ratio vs. \n Median Transition Length Ratio')
lims = [
    np.min([ax[0,1].get_xlim(), ax[0,1].get_ylim()]),  # min of both axes
    np.max([ax[0,1].get_xlim(), ax[0,1].get_ylim()]),  # max of both axes
]
ax[0,1].plot(lims, lims, 'k--', alpha=0.75, zorder=0)
ax[0,1].set_aspect('equal')
ax[0,1].set_xlim(lims)
ax[0,1].set_ylim(lims)
ax[0,1].set_aspect(1./ax[0,1].get_data_ratio())

ax[1,0].plot(x3,y3,'ko')
ax[1,0].set_xlabel('$f_i/f_w$')
ax[1,0].set_ylabel('var($l_i$)/var$(l_w)$')
ax[1,0].set_title('Ice-to-Water Ratio vs. \n Mean Transition Length Ratio')
ax[1,0].set_aspect(1./ax[1,0].get_data_ratio())

ax[1,1].plot(x4,y4,'ko')
ax[1,1].set_xlabel('$f_i/f_w$')
ax[1,1].set_ylabel('$L_p$')
ax[1,1].set_title('Ice-to-Water Ratio vs. \n Mean Integral Scale')
ax[1,1].set_aspect(1./ax[1,1].get_data_ratio())

plt.tight_layout()
plt.show()
plt.savefig('trans_frac_correlation.png')



