import plotly.graph_objs as go
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import os

title='PY-GC-MS'

if title == 'PY-GC-MS':
    DIR = 'C:\\Users\\tatab\\OneDrive\\Data\\AIAEXPRT.AIA\\TIC_data\\'
    xname = 'time'
    yname = 'count'
    autorange = True
else:
    pass

os.chdir(DIR)
print(DIR)
# mass_dict = (('18','18.1'),('28','28.1'),('32','32.1'),
#                  ('40','39.9'),('44','43.9'),('207','206.9'),
#                  ('208','207.9'),('209','208.9'),('73','73.1'),
#                  ('133','132.9'),('96','96.1'),('164','163.9'),
#                  ('250','249.9'),('191','190.9'),('356','356.1'),
#                  ('29','29.1'),('177','176.9'),('191','190.9'),
#                  ('192','191.9'),('193','192.9'),('249','248.9'),
#                  ('250','249.9'),('252','251.9'),('266','265.9'),
#                  ('266','265.9'),('267','266.9'),('282','281.9'),
#                  ('283','282.9'),('284','283.9'),('340','339.9'),
#                  ('341','340.9'),('342','341.9'),('355','355.1'),
#                  ('179','178.9'),('178','177.9'),('167','166.9'),
#                  ('163','162.9'),('147','146.9'),('135','134.9'),
#                  ('134','133.9'),('132','131.9'),('125','124.9'),
#                  ('121','121.9'),('119','118.9'),('117','116.9'),
#                  ('116','115.9'),('115','114.9'),('103','102.9'))
# df =  df.drop(['17.1','18','18.1','28','28.1','29','29.1','32','32.1','40','44','206.9','207','207.9','208','208.9','209','73.1','73','96','132.9','133','147','96.1','164','163.9','177','176.9','190.9','191','191.9','192','192.9','193','248.9','249','249.9','250','251','265','266','266.9','267','281','282','283','284','340','340.9','341','342','355','355.1','356','356.1'],axis=1)
# df['17.1'] = df['17.1'] - df['17.1'].median()
# df.ix[np.isnan(df['18.1']), ['18']] = df.ix[np.isnan(df['18.1']), ['18']] - df['18.1'].median()
# def adjust_mz(df):
#     df['17.1'] = df['17.1'] - df['17.1'].median()
#     df.columns_temp = df.columns.copy()
#     df.columns = df.columns.astype(float)
#     temp = df.columns.values
#     margin = 0.101
#     for n in np.arange(170, 500, 10):
#         l = n - 0.1
#         m = n + 0.1
#         calc_n = np.where(np.abs(temp - n) < margin)
#         df[n] = df.iloc[:, calc_n[0]].sum(axis=1)
#
#         calc_l = temp[np.where(temp == l)]
#         calc_m = temp[np.where(temp == m)]
#         df[calc_l] = 0
#         df[calc_m] = 0
#     df.columns = df
def adjust_mz(df):
    df.columns_temp = df.columns.copy()
    df.columns = df.columns.astype(int)
    col_values = df.columns.values
    margin = 5

    for n in np.arange(col_values.min(), col_values.max(), 10):
        calc_n = np.where(temp - n < 0 and np.abs(temp - n) < margin)
        print(calc_n)
        df[n] = df.iloc[:, calc_n[0]].sum(axis=1)

        calc_l = temp[np.where(temp == l)]
        calc_m = temp[np.where(temp == m)]
        df[calc_l] = 0
        df[calc_m] = 0
        if n == col_values.min():
            pressed_df = pd.Dataframe()
    df.columns = df.columns_temp
    return df

def erase_bk(df,name=None,save = 0):
    if name == '0607BaseLine.CDF.csv':
        return
    Base = pd.read_csv('0607BaseLine.CDF.csv', header=1, index_col='time')
    Base = adjust_mz(Base)
    df = adjust_mz(df)
    Base.index = df.index
    df1 = df
    erased_df = df1.sub(Base, fill_value=0)
    # df =  df.drop(['17.1','18','18.1','28','28.1','29','29.1','32','32.1','40','44','206.9','207','207.9','208','208.9','209','73.1','73','96','132.9','133','147','96.1','164','163.9','177','176.9','190.9','191','191.9','192','192.9','193','248.9','249','249.9','250','251','265','266','266.9','267','281','282','283','284','340','340.9','341','342','355','355.1','356','356.1'],axis=1)
    if save == 1:
        name = name.replace(".\\", "")
        name = name.replace(".CSV", "")
        name = name.replace(".CFD", "")
        erased_df[erased_df < 0] = 0
        erased_df[erased_df == 0] = np.nan

        erased_df.to_csv(name+'_remove_base.csv')
    else:
        pass

    erased_df[erased_df < 0] = 0
    erased_df = erased_df.fillna(0)
    print('erase')
    return df

    # df = df.sum(axis=1)
    # import  pylab as plt
    # df.plot()
    # plt.scatter(x=df.columns.values,y=df2.values.tolist())
    # plt.show()
def serch_peak_top(df):
    df = df.sum(axis=1)
    df_diff1 = df.diff(1)
    df_diff2 = df_diff1.diff(1)
    df_diff3 = df_diff2.diff(1)


def Data_compression(df,save=0):
    pass



if __name__ == '__main__':
    import glob
    file_names = glob.glob('./*CSV')
    for num, name in enumerate(file_names):
        print(name)
        df = pd.read_csv(name, header=1, index_col='time')
        df = erase_bk(df,name,save=1)
        serch_peak_top(df)

