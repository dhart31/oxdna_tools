import numpy as np
import pandas as pd

# Convert oxDNA units
k = 1*57.09 # sim units * pn/nM
xunit = 0.8518 # nm

# Generate dataframe of mean force-extensions

def get_forceextensions_dataframe(state,r0_vals,r0_names):
	df = pd.DataFrame()
	for idx,r0_val in enumerate(r0_vals):
		temp = pd.DataFrame()
		x_array = np.loadtxt(state+"_distance_"+r0_names[idx]+".dat")
		x = np.mean(x_array)*xunit
		temp['x'] = [x]
		dx = abs(x-r0_val*xunit)
		temp['r0'] = [r0_val]
		temp['dx'] = dx
		temp['force'] = dx*k
		temp['probestate'] = state
		df = pd.concat([df,temp],ignore_index=True)
	return df

# Get unbound state force extension dataframe
r0_vals_ub =  [ 6.0 , 6.2 , 6.4,6.6]
r0_names_ub = ['6p0','6p2','6p4','6p6']
df_ub =  get_forceextensions_dataframe('unbound',r0_vals_ub,r0_names_ub)

# Get bound state force extension dataframe
r0_vals_b =  [ 6.4 , 6.5 , 6.6 , 6.7]
r0_names_b = ['6p4','6p5','6p6','6p7']
df_b   = get_forceextensions_dataframe('bound',r0_vals_b,r0_names_b)

# Get middle pair state force extension dataframe
r0_vals_t =  [ 6.5 , 6.75, 7,  7.25,  7.5]
r0_names_t = ['6p5','6p75','7','7p25','7p5']
df_mid = get_forceextensions_dataframe('middle',r0_vals_t,r0_names_t)

# Get end pair state force extension dataframe
r0_vals_t =  [6.5,6.625, 6.75, 6.875,7]
r0_names_t = ['6p5','6p625','6p75','6p875','7']
df_end = get_forceextensions_dataframe('end',r0_vals_t,r0_names_t)

df = pd.concat([df_ub,df_mid,df_end,df_b],ignore_index=True)
df.to_pickle('forceextensions_mean.pkl')
