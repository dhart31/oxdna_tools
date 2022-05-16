import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# INPUT: dataframe of mean stacking energy values ("get_stacking_energy_dataframe.py"), where each row is a unique molecule. 
# OUTPUT: plot of mean stacking energy

fig = plt.figure(figsize = [4,4],constrained_layout=True)
ax = fig.add_subplot()

mean_stacking_energy_vals = pd.read_pickle('mean_stacking_bows.pkl')
mean_stacking_energy_vals = np.transpose(mean_stacking_energy_vals['mean'])*(3000/(273+22))

x = np.arange(0,7)
y = mean_stacking_energy_vals
plt.plot(x,y,marker='o',linewidth=2,color='black')

ax.tick_params(labelsize=10)
xticklabels = ['0','74','84','105','126','158','210','252'] # 0 put there for offset, don't know why its necessary
ax.set_xticklabels(xticklabels,rotation=0)	
plt.xlabel('dsDNA Bow Size (bp)',fontsize=12)
plt.ylabel('Average Stacking Potential (kT)',fontsize=12)
plt.title('Average Dinucleotide Stacking \n Potential of ssDNA Target Strand',fontsize=14)
plt.savefig('bow_stacking_energy.pdf',dpi=300)
plt.show()
