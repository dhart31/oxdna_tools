import pandas as pd

def calculate_ffs_rate(df,state):
	if state == 'bound':
		dt = 0.003*3.03e-12*(1/60) # minutes
	else:
		NA = 6.02214086e23 #Avogadro's constant molecules per mole
		V = (0.8518e-9*12)**3*1000 # estimate volume of box, in liters
		M = (1/NA)*(1/V) # Molar (mol/liter)
		dt = 0.003*3.03e-12*M*1e6 # seconds*microMolar
	df_mean = df.groupby(['ffs_step']).mean()
	flux = df_mean['flux'].iloc[0]/dt
	shoot = df_mean['success_prob'].iloc[1]
	prune = df_mean['prune_success_prob'].iloc[2:].prod()
	print(flux*shoot*prune)

df = pd.read_pickle('../data/b_6p5_03-07.pkl')
df2 = pd.read_pickle('../data/ub_6p0_03-07.pkl')

calculate_ffs_rate(df,'bound')

calculate_ffs_rate(df2,'unbound')


