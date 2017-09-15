import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3,3))
df.index=['a','b','c']
df.columns=['d','e','f']

print(df)
print(df.T)
df['time'] =['h','i','j']
print(df[0:1])
df.columns =df[0:1]
print(df)