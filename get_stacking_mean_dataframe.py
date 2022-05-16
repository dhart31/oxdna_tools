import numpy as np
import pandas as pd
bow_sizes = [74,84,105,126,158,210,252]

df = pd.DataFrame()
vals_mean = np.empty(len(bow_sizes))
vals_std = np.empty(len(bow_sizes))
for i,bow_size in enumerate(bow_sizes):
        data = np.loadtxt('outputs/stacking_circle'+str(bow_size)+'_2.dat')
        vals_mean[i] = np.mean(data[0:75000,4::11])
        vals_std[i] =  np.std(data[0:75000,4:11])
df['mean'] = vals_mean
df['std'] = vals_std
df.to_pickle('mean_stacking_bows.pkl')

