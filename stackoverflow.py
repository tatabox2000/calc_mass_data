import pandas as pd
import  numpy as np

df = pd.DataFrame(data= np.arange(0,10000,1).reshape(100,100))
df.columns = np.arange(0,10,0.1)

df.columns = df.columns.astype(float)
temp = df.columns.values

for n in np.arange(1, 9, 1):
    margin = 0.101     # set your own margin
    calc_n = np.where(np.abs(temp-n) < margin)
    print(calc_n)
    print(calc_n[0])
    df[n] = df.iloc[:,calc_n[0]].sum(axis=1)

"""
for n in np.arange(1, 9, 1):
    l = n - 0.1
    m = n + 0.1
    calc_n = temp[np.where((temp >= l) & (temp <= m))]
    calc = np.sum(df[df.columns.intersection(calc_n)], axis=1)
    n_position = temp[np.where(temp == n)]
    df[n_position] = calc.values
    """