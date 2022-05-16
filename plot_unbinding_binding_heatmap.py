import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import (ScalarFormatter, MultipleLocator)
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

fontsize=10

#Subplot grid
titles = ['A) Unbinding','B) Binding']
fig, big_axes = plt.subplots(figsize = [4.25,4.25],nrows=2,ncols=1,constrained_layout=True)
for row, big_ax in enumerate(big_axes):
    big_ax.set_title(titles[row], fontsize=16,loc = 'center',y = 1,pad=5)
    big_ax.axis('off')
    big_ax._frameon = False

#Plot settings
plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r'\usepackage{siunitx} \sisetup{detect-all} \usepackage{helvet} \usepackage{sansmath} \sansmath', 
    "mathtext.default":"regular"
})

## BOUND MEAN INTERACTION POTENTIALS, PAIRING AND STACKING

#PAIRING HEATMAP
E0 = 3000/(273+22)
vmin = E0*0
vmax = E0*-0.7
df = pd.read_pickle("../data/bp_b_6p5_final_03-07_mean.pkl")

#PAIRING HEATMAP DATA
vals = np.empty((0,9),float)
for name,group in df.groupby('num_bp'):
	vals = np.append(vals,[np.array(group['bp_energy'])],axis=0)		
vals[[0,1],:] = vals[[1,0],:] #rearrange 0 bp and 0.85 nm

#PAIRING HEATMAP PLOTTING
ax = fig.add_subplot(2,2,1)
sns.heatmap(np.flip(vals,0)*E0,ax=ax,cmap='magma',cbar=True,cbar_kws={"shrink": .50},square=True,vmin=vmin, vmax=vmax)

#PAIRING HEATMAP LABELING
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=8)
cbar.set_label('$k_BT$',rotation='horizontal',labelpad=10)
ax.tick_params(axis=u'both', which=u'both',length=0,labelsize=8)	
xticks = [-.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5]
xticklabels=['G\nl\nC','T\nl\nA','A\nl\nT','A\nl\nT','A\nl\nT','T\nl\nA','T\nl\nA','C\nl\nG','A\nl\nT']
yticklabels = [str(i)+' bp' for i in range(8,-1,-1)]+['$>0.85$ nm']
ax.set(xticks = np.linspace(.5,8.5,9),xticklabels=xticklabels,yticks = np.linspace(0.5,9.5,10))
ax.set_yticklabels(yticklabels,rotation=0)
ax.text(-1,14,'5\'\n\n3\'',fontsize=8)
ax.set_title("Base Pairing Energy", x = 0.5,y=1.02, pad=7.5,fontsize=fontsize)
#ax.text(-0.3,1.1,'A',fontsize=16,transform=ax.transAxes)

#STACKING HEATMAP
vmin = -E0*0.96
vmax = -E0*1.2
xticklabels = ['G\nC','\n-','T\nA','\n-','A\nT','\n-','A\nT','\n-','A\nT','\n-','T\nA','\n-','T\nA','\n-','C\nG','\n-','A\nT']
df = pd.read_pickle("../data/stacking_b_6p5_final_03-07_mean.pkl")

#STACKING HEATMAP DATA
vals = np.empty((0,25),float)
for name,group in df.groupby('num_bp'):
	vals = np.append(vals,[np.array(group['stacking'])],axis=0)
vals[[0,1],:] = vals[[1,0],:]

#STACKING HEATMAP PLOTTING
ax = fig.add_subplot(2,2,2)
sns.heatmap(np.flip(vals[:,4:12],0)*E0,ax=ax,cmap='magma',cbar=True,square=True,cbar_kws={"shrink":.50},fmt='.2f',vmin=vmin,vmax=vmax)

#STACKING HEATMAP LABELING
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=8)
cbar.set_label('$k_BT$',rotation='horizontal',labelpad=10)
ax.tick_params(axis=u'both', which=u'both',length=0,labelsize=8)	
ax.set(xticks = np.linspace(0,8,17),xticklabels=xticklabels,yticks = np.linspace(0.5,9.5,10))
ax.set_yticklabels(yticklabels,rotation=0)
ax.text(-1.5,12.4,'5\'\n3\'',fontsize=8)
ax.set_title("Stacking Energy", x = 0.5,y=1.01, pad=5,fontsize=fontsize)	

## UNBOUND MEAN INTERACTION POTENTIALS, PAIRING AND STACKING


#PAIRING HEATMAP
vmin = E0*0
vmax = E0*-0.7
xticks = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5]
xticklabels=['G\nl\nC','T\nl\nA','A\nl\nT','A\nl\nT','A\nl\nT','T\nl\nA','T\nl\nA','C\nl\nG','A\nl\nT']
yticklabels = ['$<1.70$ nm','$<0.85$ nm','1 bp','2 bp','3 bp','4 bp','5 bp','6 bp ','7 bp', '8 bp','9 bp']

df = pd.read_pickle("../data/bp_ub_6p0_final_03-07_mean.pkl")

#PAIRING HEATMAP DATA
vals = np.empty((0,9),float)
for name,group in df.groupby('num_bp'):
	vals = np.append(vals,[np.array(group['stacking'])],axis=0) #mislabeled as stacking, but I double checked that its base pair energy
vals[[0,1,2],:] = vals[[2,0,1],:] # rearrange [0.85 nm, 1.7 nm, 1 bp] into [1.7 nm, 0.85 nm, 1 bp], which otherwise are sorted numerically

#PAIRING HEATMAP PLOTTING
ax = fig.add_subplot(2,2,3)
sns.heatmap(vals*E0,ax=ax,cmap='magma',cbar=True,cbar_kws={"shrink": .50},square=True,vmin=vmin, vmax=vmax)

#PAIRING HEATMAP LABELING
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=8)
cbar.set_label('$k_BT$',rotation='horizontal',labelpad=10)
ax.tick_params(axis=u'both', which=u'both',length=0,labelsize=8)	
ax.set(xticks = np.linspace(0.5,8.5,9),xticklabels=xticklabels,yticks = np.linspace(0.5,10.5,11))
ax.text(-1,15,'5\'\n\n3\'',fontsize=8)
ax.set_yticklabels(yticklabels,rotation=0)
ax.set_title("Base Pairing Energy", x = 0.5,y=1.0, pad=7.5,fontsize=fontsize)

#STACKING HEATMAP
vmin = -E0*0.96
vmax = -E0*1.2
xticklabels = ['G\nC','\n-','T\nA','\n-','A\nT','\n-','A\nT','\n-','A\nT','\n-','T\nA','\n-','T\nA','\n-','C\nG','\n-','A\nT']
df = pd.read_pickle("../data/stacking_ub_6p0_final_03-07_mean.pkl")

#STACKING HEATMAP DATA
vals = np.empty((0,25),float)
for name,group in df.groupby('num_bp'):
	vals = np.append(vals,[np.array(group['stacking'])],axis=0)
vals[[0,1,2],:] = vals[[2,0,1],:] # rearrange [0.85 nm, 1.7 nm, 1 bp] into [1.7 nm, 0.85 nm, 1 bp], which otherwise are sorted numerically

#STACKING HEATMAP PLOTTING
ax = fig.add_subplot(2,2,4)
sns.heatmap(vals[:,4:12]*E0,ax=ax,cmap='magma',cbar=True,square=True,cbar_kws={"shrink":.50},fmt='.2f',vmin=vmin,vmax=vmax)

#STACKING HEATMAP LABELING
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=8)
cbar.set_label('$k_BT$',rotation='horizontal',labelpad=10)
ax.tick_params(axis=u'both', which=u'both',length=0,labelsize=8)	
ax.set(xticks = np.linspace(0,8,17),xticklabels=xticklabels,yticks = np.linspace(0.5,10.5,11))
ax.text(-1.5,13.35,'5\'\n3\'',fontsize=8)
ax.set_yticklabels(yticklabels,rotation=0)
ax.set_title("Stacking Energy", x = 0.5,y=1.0, pad=5,fontsize=fontsize)

plt.savefig('../figures/binding_unbinding_heatmaps.pdf',format='pdf',dpi=400)
fig.set_facecolor('w')
#plt.tight_layout()
plt.show()
