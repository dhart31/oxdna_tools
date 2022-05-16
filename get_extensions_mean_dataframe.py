import pandas as pd
import numpy as np
from scipy.io import savemat

# Input: oxDNA distance observable files (1 distance only)
# Output: Dataframe of mean extension/distance_values

bow_sizes = ['74','84','105','126','158','210','252']
probe_names = ['_1','b_1','_2','b_2','_2','b_3','_3','b_4']
probe_sequences = ['GTAAATTCA','GTAAATTCA','AGGACTTGT','AGGACTTGT','AGGACTTG','AGGACTTG','CAAGTCCT','CAAGTCCT']

df = pd.DataFrame()
xunit = 0.8518 # Convert to nanometers from simulation units
for idx,bow_size in enumerate(bow_sizes):
	for jdx,probe_name in enumerate(probe_names):
		filename = 'bow_sim_positions/position_circle'+str(bow_size)+probe_name+'.dat'
		pos = np.loadtxt(filename)
		ext_mean = np.mean(pos[0:75000]*xunit)
		ext_std = np.std(pos[0:75000]*xunit)
		if 'b' in probe_name:
			state = 'Bound'
		else:
			state = 'Unbound'
		df = df.append({'ext_mean':ext_mean,'ext_sd':ext_std,'bowsize':bow_size,'seq':probe_sequences[jdx],'state':state},ignore_index=True)
print(df)
savemat('bow_extensions_mean.mat',df.to_dict('list'))
df.to_pickle('bow_extensions_mean.pkl')
	
