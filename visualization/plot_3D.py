import plotly
plotly.offline.init_notebook_mode()
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
from plotly.graph_objs import *
import numpy as np
import pandas as pd
import  peakutils


def plot_3D(file_name):
    #result = pd.read_csv(DIR + file_name,index_col='time')
    result = pd.read_csv(file_name,header=1, index_col='time')
    result = result.fillna(0)
    #result = pd.read_csv(file_name,header=1)
    result.columns = result.columns.astype(float)
    #result = result.rename(columns={result.columns[0]:'time'})
    #print(result.set_index('time'))
    #print(result.columns)

    #result.columns[1:] = result.columns[1:].astype(float)
    temp = result.columns.values

    calc = temp[np.where( (temp>= 60)&(temp<=240))]
    data= result[result.columns.intersection(calc)].copy()
    #calc2 = temp[np.where( (temp>= 208) & (temp<=206))]
    #data= result[result.columns.intersection(calc2)].copy()
    data2 = data.loc[(data.index > 0) & (data.index < 800) ]

    colum_list = np.arange(0,len(data2.columns),1)
    index_list = np.arange(0,len(data2.index),1)
    data3 = data2.iloc[:,colum_list]

    colorscale=[
        [0.0,'rgb(94,79,162)'],
        [0.1,'rgb(50,136,189)'],
        [0.2, 'rgb(102,194,165)'],
        [0.3, 'rgb(171,221,164)'],
        [0.4,'rgb(230,245,152)'],
        [0.5,'rgb(255,255,191)'],
        [0.6,'rgb(254,224,139)'],
        [0.7,'rgb(253,174,97)'],
        [0.8,'rgb(244,109,67)'],
        [0.9,'rgb(213,62,79)'],
        [1.0,'rgb(158,1,66)']
    ]

    data  = [
        Surface(
            z = data3.as_matrix(),
            y = data3.index/60,
            x = data3.columns.values,
        colorscale = colorscale,
        cmax = 50,
        cmin = 0
            )
    ]
    layout = Layout(
        scene=dict(
            xaxis = dict(
                title = 'm/z'),
            yaxis = dict(
                title = 'time'),
            zaxis = dict(
                title = 'count',range = [0,200]
            )
        ),
        width=900,
        height=1000,
        margin=dict(
            l=65,r=50,b=65,t=90
        )
    )
    fig = Figure(data=data, layout=layout)
    print('ok')
    plot(fig, filename=file_name + '.html',show_link=False)

if __name__ == '__main__':
    import glob
    import os
    #DIR = 'C:\\Users\\admin\\OneDrive\\waters\\test\\'
    DIR = 'C:\\Users\\tatab\\OneDrive\\Data\\AIAEXPRT.AIA\\'
    # file_name = '170619_hai_gyou_3h_scan_3.TXT.csv'
    # file_name = '170619_hai_sayou_1h_scan_3.TXT.csv'
    #file_name = 'CELOBIOSE_75_SIM_170721.TXT.csv'
    DIR2 = DIR + '\*.csv'
    for n,name in enumerate(glob.glob(DIR2)) :
        print(name)
        plot_3D(name)
        if n == 0:
            break