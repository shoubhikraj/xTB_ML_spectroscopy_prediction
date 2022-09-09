import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../similarity_score_outlier.csv',index_col=0)

mask = np.zeros_like(df,dtype=bool)
mask[np.triu_indices_from(mask)] = True
mask[np.diag_indices_from(mask)] = True

myfigsize=(6,6)
fig, ax = plt.subplots(figsize=myfigsize)
this_cmap = sns.diverging_palette(10,220,as_cmap=True)
sns.heatmap(df,mask=mask,cmap=this_cmap,square=True,vmin=0,vmax=1,linewidths=1.1,cbar_kws={"shrink":.5})
ax.tick_params(which='major',labelsize=7)
ax.tick_params()
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize='xx-small')
#plt.show()
plt.savefig('outliers_dice_similarity.eps',dpi=600,bbox_inches='tight')