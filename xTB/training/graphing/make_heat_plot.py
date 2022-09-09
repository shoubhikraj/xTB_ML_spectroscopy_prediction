import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_train = pd.read_csv('train_set_results.csv',index_col=0)
data_test = pd.read_csv('test_set_results.csv',index_col=0)

myfigsize=(12,5)
fig,ax = plt.subplots(figsize=myfigsize)
sns.heatmap(data_train,cmap='PiYG_r',ax=ax,annot=True,fmt='.2f',linewidths=3.5,linecolor='w',annot_kws={'fontsize':'large'},vmin=0.00,vmax=0.22)
#ax.tick_params(which='major',left=False,bottom=False)
ax.tick_params(which='major',labelsize='xx-large')
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize='xx-large')
ax.set_yticklabels(ax.get_yticklabels(),rotation=0)
ax.set_xticklabels(ax.get_xticklabels(),rotation=45)
plt.tight_layout()
plt.savefig('heatmap_train_results.eps',bbox_inches='tight',dpi=600)

fig,ax = plt.subplots(figsize=myfigsize)
sns.heatmap(data_test,cmap='PiYG_r',ax=ax,annot=True,fmt='.2f',linewidths=3.5,linecolor='w',annot_kws={'fontsize':'large'},vmin=0.00,vmax=0.22)
#ax.tick_params(which='major',left=False,bottom=False)
ax.tick_params(which='major',labelsize='xx-large')
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize='xx-large')
ax.set_yticklabels(ax.get_yticklabels(),rotation=0)
ax.set_xticklabels(ax.get_xticklabels(),rotation=45)
plt.tight_layout()
plt.savefig('heatmap_test_results.eps',bbox_inches='tight',dpi=600)


