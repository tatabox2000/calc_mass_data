import numpy as np
import pylab as plt
import os
import glob
import pandas as pd
import seaborn as sns
plt.style .use('dark_background')
place = 'C:\\Users\\admin\\OneDrive\\waters\\test'
os.chdir(place)
File_names = glob.glob('*')
for File_name in File_names:
    temp_df = pd.read_table(File_name,header=0,names=['data_names','value','Nodata'])
    a,b=0,0
    list = []
    for number in temp_df[temp_df['data_names'] =='Retention Time'].index:
        a = b
        b = number
        if b == 1:
            pass
        else:
            for times in np.arange(0,b-a,1):
                list.append(temp_df['value'][a])
    for last_times in np.arange(0,len(temp_df.index)-b+1,1):
        list.append(temp_df['value'][b])
    print(temp_df.shape)
    print(len(list))
    temp_df['time']=list
    result = pd.Series([])
    for name in set(temp_df['data_names']):
        if name == 'Retention Time':
            pass
        elif name == 'Scan':
            pass
        else:
            temp2_df = temp_df[temp_df['data_names'] == name].copy()
            temp2_df.rename(columns={'value' : name},inplace=True)
            if result.empty:
                result = temp2_df[['time' , name]]
            else:
                result = pd.merge(result, temp2_df[['time' , name]], on='time', how='outer')
                print('now copying')
    Final_resut_temp = result.set_index('time').fillna(0)
    Final_resut = Final_resut_temp.sort_index(axis=1, ascending=True).copy()
    result_name = place + '\\' + File_name + '.csv'
    Final_resut.to_csv(result_name)
    print('Finished')