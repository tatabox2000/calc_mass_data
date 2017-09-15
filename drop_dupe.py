import numpy as np
import  pandas as pd
DIR = 'C:\\Users\\admin\\OneDrive\\Data\\'


df = pd.read_csv(DIR + 'test1-02.CDF.csv',header=None)
#temp1 = df.columns.values.astype(np.float64)

temp1 = df.iloc[0,:]
name1,name2 = 0,0
drop_columns = []
drop_num = []
for num,mz in enumerate(temp1):
    if name1 == '':
        pass
    elif name1 == 0:
        name1 = mz
    else :
        name2 = mz
        chack_dupe = name2 - name1
        if chack_dupe == 0:
            drop_columns.append(num)
            drop_num.append(name2)
        name1 = name2
df2 = df.drop(drop_columns,axis=1)
print(df2.shape)
np.savetxt(DIR + 'result.csv',df2,delimiter=",")
#df2.to_csv(DIR + 'result.csv',index_col=0)


