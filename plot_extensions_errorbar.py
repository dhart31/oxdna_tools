import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.lines as mlines

sns.set_style('whitegrid')
df = pd.read_pickle('bow_extensions.pkl')
bow_names = ['74','84','105','126','158','210','252']
df.bowsize = pd.Categorical(df.bowsize, categories=map(str, bow_names), ordered=True)
g = sns.catplot(x='bowsize', y='x', data=df, col='seq',hue='state',kind='point',aspect=1,height=3,col_wrap=2,palette=['black','gray'],ci='sd',legend=False,capsize=0.2,dodge=.25)

bound = mlines.Line2D([], [], color='gray',markeredgecolor='gray', marker='o', linestyle='None', markersize=8, label='Bound')
unbound = mlines.Line2D([], [], color='black',markeredgecolor='black', marker='o', linestyle='None', markersize=8, label='Unbound')

plt.legend(handles=[bound,unbound],loc = "center", bbox_to_anchor=(0.8,0.9),framealpha=1)
g.set_axis_labels("Bow Size (bp)", "Extension (nm)")
g.set_titles(col_template="{col_name}",fontsize=24)
plt.tight_layout()
#plt.savefig('bowsims_avgposition.pdf',dpi=300)
plt.show()

