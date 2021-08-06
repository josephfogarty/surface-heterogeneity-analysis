# getting some plots

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

plt.close('all')

# load in csv
df = pd.read_csv('test_semivar.csv')

maps = ['b','e','c']
labels = ['Beaufort Sea', 'E. Siberian Sea', 'Fram Strait']

# get rx
rx = df['rx']

def lp(row,rx):
    # row is a pandas series
    # rx is dimensional length of translation vector
    return sum((1-row))*rx
    

# plot 3
fig_x, ax_x = plt.subplots(figsize=(7.5,4.5))
for s in range(len(maps)):
    semivar = df[f'semivar_{maps[s]}']
    ax_x.plot(rx,semivar,label=f'{labels[s]}, $L_p={lp(semivar,50):.1f}$ m')
ax_x.set_xlabel(r'$r_x$ (m)',fontsize=20)
ax_x.set_ylabel(r'$D_{\theta\theta}/D_{\theta\theta,max}$',fontsize=20)
ax_x.tick_params(labelsize=16)
ax_x.legend(fontsize=16)
ax_x.set_title("Surface Temperature Semivariograms",fontsize=16)
fig_x.tight_layout()
#fig_x.savefig(os.path.join(semivariogram_sp,fname + '_x.png'))
plt.show()
