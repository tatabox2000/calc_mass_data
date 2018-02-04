import numpy as np
import netCDF4 as cdf
import glob
import os
import pandas as pd
import pylab as plt
import math
import sys

class cfd_to_csv_and_restruct:
    def __init__(self):
        self.__ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.__EXE_PATH = sys.executable
        self.__ENV_PATH = os.path.dirname(self.__EXE_PATH)
        self.__LOG = os.path.join(self.__ENV_PATH, 'log')

    def cut_dupe(self,mass):
        mass = np.round(mass)
        mass_chack = mass.copy()
        mass_chack = np.insert(mass_chack, 0, 0)
        mass_chack = np.delete(mass_chack, mass_chack.shape[0] - 1)
        mass_result = mass - mass_chack
        mass_result[mass_result<-10]=1
        #dupe = mass_result[np.where(mass_result == 2)]
        nodata = np.where(mass_result == 2)
        triple = np.where(mass_result==3)
        dupe = np.where(mass_result == 0)
        mass_result[dupe] = 1000
        mass_result[nodata] =500
        mass_result[triple] = 1500
        dupe_num = mass_result

        print(dupe_num)
        x = np.arange(0,mass.shape[0],1)
        plt.scatter(x,dupe_num,s=1)
        plt.show()

        #print(mass)
        """
        num1, num2 = 0, 0
        for n, mz in enumerate(mass):
            if num1 == 0:
                num1 = mz
            else:
                num2 = mz
                if num2 - num1 == 1:
                    num1 = num2
                elif num2 - num1 == 0:
                    print(num1,num2)
                    mass[n] = mass[n - 1] + 1
                    num1 = mass[n]
                    print('number=',n)
                elif num2 - num1 < 0:
                    pass
                    #print(num2 - num1)
                elif n >5000:
                    break
    
                    #print(n)
    
        mass_chack = mass.copy()
        mass_chack = np.insert(mass_chack, 0, 0)
        mass_chack = np.delete(mass_chack, mass_chack.shape[0] - 1)
        mass_result = mass - mass_chack
        dupes_high = np.where(mass_result == 2)
        for dupe in dupes_high:
            mass[dupe] = mass[dupe - 1] + 1
        dupes_low = np.where(mass_result == 0)
        for dupe in dupes_low:
            mass[dupe] = mass[dupe - 1] + 1
        print(mass[dupe], mass[dupe - 1])
    
        return mass
        """
    def cfd_to_CSV(self,file_names):
        for file_name in file_names:
            #print(file_name)
            cdf_file = cdf.Dataset(file_name)

            time = np.array(cdf_file.variables['scan_acquisition_time'][:])
            time = np.insert(time,0,'0')
            mass = np.array(cdf_file.variables['mass_values'][:]*10).astype(int)
            print(mass.min()/10)
            point = np.array(cdf_file.variables['point_count'][:])
            #index = np.round(np.arange(np.round(mass.min(),decimals=0),np.round(mass.max(),decimals=0),1),decimals=0).T
            index = np.arange(math.floor(mass.min()/10)*10,math.ceil(mass.max()/10)*10+1,1).T.astype(int)

            print(index)
            #results.index.astype(int)
            results = pd.DataFrame(index,columns=['mz'])
            #results.index = results['mz']
            #results= results.drop('mz',axis=1)
            print(results)

            #dupe
            mass_round = np.around(mass)
            mass_range = mass_round - mass
            plt.scatter(np.arange(0,mass.shape[0],1),mass_range,s=1)
            plt.show()

            #mass = cut_dupe(mass)

            #print(point.shape)
            #plt.scatter(np.arange(0,point.shape[0],1),point,s=1)
            #plt.show()
            DATA = np.array(cdf_file.variables['intensity_values'][:])
            point = np.array(cdf_file.variables['point_count'][:])
            values = np.array([np.round(mass*10), DATA]).T
            values = pd.DataFrame(values)
            values.columns = ['mz', 'count']
            values.index.astype(str).astype(int)
            n, n1 = 0, 0
            len, len2 = 0, 0
            for num in point:
                if n == 0:
                    result2 = values.iloc[0:num - 1]
                    results = pd.merge(results,result2, on='mz', how='left')
                    n = num
                elif n > 0:
                    n1 = n + num
                    result2 = values.iloc[n:n1 - 1]
                    # result= result.join(result2,how='outer')
                    # result = pd.concat([result,result2],axis=1)
                    results = pd.merge(results,result2, on='mz', how='left')
                    n = n1
                    #print(results.head())
                    #print(results.shape)
            #results=results.fillna(0)
            results['mz']=results['mz']
            results=results.T
            #print(results.shape)
            #print(time.shape)

            results.index=time
            #np.savetxt(file_name +'.csv')
            results.to_csv(file_name +'.csv')
        #np.savetxt('time.csv',time,delimiter=",")
        #np.savetxt('mass.csv',mass,delimiter=",")
        #np.savetxt('data.csv',DATA,delimiter=",")
        #np.savetxt('point.csv',point,delimiter=",")

#if __name__ == '__main':
DIR = 'C:\\Users\\tatab\\OneDrive\\Data\\島津'
os.chdir(DIR)
file_names = glob.glob('*.CDF')

cfd_to_csv_and_restruct = cfd_to_csv_and_restruct()
cfd_to_csv_and_restruct.cfd_to_CSV(file_names)