import numpy as np
import netCDF4 as nc
import glob
import os
import pandas as pd

DIR = 'C:\\Users\\admin\\OneDrive\\Data\\'
os.chdir(DIR)
file_names = glob.glob('*.CDF')

for file_name in file_names:
    print(file_name)
    cdf_file = nc.Dataset(DIR + file_name)
    time = np.array(cdf_file.variables['scan_acquisition_time'][:])
    print(time)
    time = np.append(time,1)
    mass = np.array(cdf_file.variables['mass_values'][:])
    DATA = np.array(cdf_file.variables['intensity_values'][:])
    point = np.array(cdf_file.variables['point_count'][:])
    values = np.array([mass,DATA]).T
    values = pd.DataFrame(values,columns=['mz','count'])
    n,n1 =0,0
    len,len2 = 0,0
    """
    for num in point:
            if n == 0:
                result = values.iloc[0:num-1]
                n = num
            elif n > 0 :
                n1 = n + num
                result2 = values.iloc[n:n1-1]
                result= result.join(result2,how='outer')
                result = pd.concat([result,result2],axis=1)
                result = result.merge(result2, on='mz',how='outer')
                n = n1
                print(n1/466)
                
                len = result.shape[0]
                len2 = len
                print(n1/466)
                if len != 465:

                    print(len)
                    result.to_csv('ire1.csv')
                    result2.to_csv('ire.csv')
                    break
                    """
    print(result.shape)
    result=result.T
    print(result.shape)
    print(time.shape)

    result.index=time
    #np.savetxt(file_name +'.csv')
    #result.to_csv(file_name +'.csv')
#np.savetxt('time.csv',time,delimiter=",")
#np.savetxt('mass.csv',mass,delimiter=",")
#np.savetxt('data.csv',DATA,delimiter=",")
#np.savetxt('point.csv',point,delimiter=",")

if __name__ == '__main':
    import netCDF4 as cdf
