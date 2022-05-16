import pandas as pd
import numpy as np
from scipy.io import savemat

# Input: oxDNA distance observable files (1 distance only)
# Output: Dataframe of extension/distance_values

bow_sizes = ['74','84','105','126','158','210','252']
probe_names = ['_1','b_1','_2','b_2','_2','b_3','_3','b_4']
probe_sequences = ['GTAAATTCA','GTAAATTCA','AGGACTTGT','AGGACTTGT','AGGACTTG','AGGACTTG','CAAGTCCT','CAAGTCCT']

df = pd.DataFrame()
xunit = 0.8518 # Convert to nanometers from simulation units
for idx,bow_size in enumerate(bow_sizes):
	for jdx,probe_name in enumerate(probe_names):
		df_temp = pd.DataFrame()
		filename = 'bow_sim_positions/position_circle'+bow_size+probe_name+'.dat'
		x = np.loadtxt(filename)
		df_temp['x'] = x[0:75000]*xunit
		if 'b' in probe_name:
			df_temp['state'] = 'Bound'
		else:
			df_temp['state'] = 'Unbound'
		df_temp['bowsize'] = bow_size
		df_temp['seq'] = probe_sequences[jdx]
		df = pd.concat([df,df_temp],ignore_index=True)
print(df)
df.to_pickle('bow_extensions.pkl')
	
