import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.lines as mlines
import matplotlib.patches as patch
import numpy as np
from scipy.stats import linregress
from scipy.io import loadmat
from scipy.io import savemat

#Plot settings
plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r'\usepackage{siunitx} \sisetup{detect-all} \usepackage{helvet} \usepackage{sansmath} \sansmath', 
    "mathtext.default":"regular"
})
sns.set_context('paper',font_scale=1.25)
sns.set_style('whitegrid')
_, ax = plt.subplots(figsize=(4,4))


palette = sns.color_palette("tab10",10)

# OXDNA MUTUAL TRAP PLOTTING

# Read force extensions of mutual trap simulations
df = pd.read_pickle('force_extensions.pkl')
x_array = [np.array(df[df.probestate==i]['x']) for i in df.probestate.unique()]
f_array = [np.array(df[df.probestate==i]['force']) for i in df.probestate.unique()]
savemat(mdict={'x_array':[list(i) for i in x_array],'f_array':[list(j) for j in f_array],'state':list(df.probestate.unique())},file_name='x_vs_f.mat')

for s,m in zip(df['probestate'].unique(),["o", "^", "v","s"]):
	if s == 'unbound' or s=='bound': # For comparing DNA bow WLC calculation to mutual trap calculation
		sns.lineplot(data=df[df['probestate']==s],y='x',x='force',marker=m,linestyle='--',markersize=10,ax=ax)

# Make legend depicting the duplex state: unbound, bound, and two transition states
#unbound = mlines.Line2D([], [], color=palette[0], marker='o', linestyle='None',markersize=8, label='Unbound')
#middle = mlines.Line2D([], [], color=palette[1], marker='^', linestyle='None',markersize=8, label='Transition \n (middle-paired)')
#end = mlines.Line2D([], [], color=palette[2], marker='v', linestyle='None',markersize=8, label='Transition \n (end-paired)')
#bound = mlines.Line2D([], [], color=palette[3], marker='s', linestyle='None',markersize=8, label='Bound')
#leg1 = ax.legend(handles=[unbound,bound,middle,end],loc = "upper left", bbox_to_anchor=(-0.02,1.02),prop={'size':10},borderpad=0.2)
#ax.set(ylim=(5,6.5),xlim=(0, 7))

# WLC PLOTTING

# Read bow force extensions from matlab WLC calculation
data = loadmat('bow_force_extensions.mat')
df_bow = pd.DataFrame({"seq":data["seq"],"bowsize":data["bowsize"][0],"ext_mean":data["ext_mean"][0],"force_mean":data["force_mean"][0],"state":data["state"]})

# Plot mutual trap oxDNA data along with DNA bow data
sns.scatterplot(data=df_bow[df_bow['seq']=='GTAAATTCA'],y='ext_mean',x='force_mean',style='state',markers = ['o','s'],s=80,linewidth=1.5,edgecolor=(palette[0],palette[1]),color='white',ax=ax,zorder=2)

# Make two legends, depicting both the probe state and pulling method (multual trap "harmonic spring", or DNA bow)
ub_spring = mlines.Line2D([],[],linestyle='None',marker='s',markersize=8,markerfacecolor=palette[1],markeredgecolor=palette[1], label='Bound')
b_spring = mlines.Line2D([],[],linestyle='None',marker='o',markersize=8,markerfacecolor=palette[0],markeredgecolor=palette[0], label='Unbound')
leg2 = ax.legend(title = 'Probe State',handles=[ub_spring,b_spring], loc='upper left',prop={'size':10},borderpad=0.2)
ub_wlc = patch.Patch(facecolor='black',edgecolor='black', label='Harmonic spring')
b_wlc = patch.Patch(facecolor='white',linewidth=1.5,edgecolor='black', label='DNA bow')
leg3 = ax.legend(title = 'Pulling method',handles=[ub_wlc,b_wlc], loc='upper left',bbox_to_anchor=(0.35,1),prop={'size':10},borderpad=0.2)
ax.add_artist(leg2)
ax.set(ylim=(5,6),xlim=(0, 7))

plt.ylabel('Extension (nm)')
plt.xlabel('Force (pN)')
plt.tight_layout()
#plt.savefig('forceextensions_dna.pdf',dpi=300)
#plt.savefig('forceextensions_spring_vs_bow.pdf',dpi=300)
plt.show()
