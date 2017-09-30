import plotly
plotly.offline.init_notebook_mode()
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
from plotly.graph_objs import *
import numpy as np
import pandas as pd

def plot_Heatmap(file_name):
    df = pd.read_csv(file_name,header=1, index_col='time')
    df = df.fillna(0)
    df.columns = df.columns.astype(float)
    temp = df.columns.values
    calc = temp[np.where((temp >= 60) & (temp <= 300))]
    data = df[df.columns.intersection(calc)].copy()
    data2 = data.loc[(data.index > 0) & (data.index < 10000)]
    data = Data(
        [Heatmap(
            z = data2.values.tolist(),
            y = data2.index/60,
            x = data2.columns.values,
            colorscale=[
                [0.0, 'rgb(94,79,162)'],
                [0.1, 'rgb(50,136,189)'],
                [0.2, 'rgb(102,194,165)'],
                [0.3, 'rgb(171,221,164)'],
                [0.4, 'rgb(230,245,152)'],
                [0.5, 'rgb(255,255,191)'],
                [0.6, 'rgb(254,224,139)'],
                [0.7, 'rgb(253,174,97)'],
                [0.8, 'rgb(244,109,67)'],
                [0.9, 'rgb(213,62,79)'],
                [1.0, 'rgb(158,1,66)']
            ],
            zmax=150,
            zmin=1

        )
    ]
    )

    plot(data,filename=file_name +'temp.html')


if __name__ == '__main__':
    import glob
    import os
    DIR = 'C:\\Users\\tatab\\OneDrive\\Data\\AIAEXPRT.AIA\\'
    DIR2 = DIR + '\*.csv'
    for n,name in enumerate(glob.glob(DIR2)) :
        print(name)
        plot_Heatmap(name)
        #if n == 3:
           #break