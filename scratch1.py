import numpy as np
import pandas as pd
import anndata as ad
print(ad.__version__)

# number of observations
n_obs = 1000
# say we measure the time of observing the data points
# add them to a dataframe for storing some annotation
obs = pd.DataFrame()
obs['time'] = np.random.choice(['day 1', 'day 2', 'day 4', 'day 8'], n_obs)
# set the names of variables/features to the following
# ['A', 'B', 'C', ..., 'AA', 'BB', 'CC', ..., 'AAA', ...]
from string import ascii_uppercase
var_names = [i*letter for i in range(1, 10) for letter in ascii_uppercase]
# number of variables
n_vars = len(var_names)
# dataframe for annotating the variables
var = pd.DataFrame(index=var_names)
# the data matrix of shape n_obs x n_vars
X = np.arange(n_obs*n_vars).reshape(n_obs, n_vars)

# we're using an integer data type just for prettier outputs
# the default 'float32' is flexible and precise enough for most purposes
adata = ad.AnnData(X, obs=obs, var=var, dtype='int32')

print(adata)

print(adata.obs_names[:10].tolist())
print(adata.obs_names[-10:].tolist())
print(adata.var_names[:10].tolist())
print(adata.var_names[-10:].tolist())


print('adata.X ------->>>>>>')
print('*********')
print(adata.X)


print('adata   ------>>>>')
print('**************"')
print(adata)

adata[:, 'A']