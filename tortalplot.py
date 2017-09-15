import plotly
plotly.offline.init_notebook_mode()
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
from plotly.graph_objs import *
import numpy as np
import pandas as pd


import plotly.graph_objs as go
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import os
import glob
import pylab as plt



#title = "IR"
#title='Raman'
title='GC-MS'


if title == 'IR':
    DIR = "C:\\Users\\admin\\OneDrive\\IR_Raman_TG\\IR\\"
    xname = 'cm-1'
    yname = 'abs'
    autorange = 'reversed'
elif title == 'Raman':
    DIR = "C:\\Users\\tatab\\OneDrive\\IR_Raman_TG\\Raman\\"
    xname = 'cm-1'
    yname = 'count'
    autorange = 'reversed'

elif title == 'GC-MS':
    #DIR = "C:\\Users\\tatab\\OneDrive\\Data\\170821_CNF_PYGCMS csv"
    DIR = 'C:\\Users\\tatab\\OneDrive\\Data\\AIAEXPRT.AIA\\'

    xname = 'time'
    yname = 'count'
    arutorange = True


os.chdir(DIR)

file_names = glob.glob('./*CSV')
left,right = 0,0
for num,name in enumerate(file_names):
    #df = pd.read_csv(name)
    df = pd.read_csv(name,header=1,index_col='time')
    df = df.fillna(0)
    df = df.sum(axis=0)
    print(df.head())
    plt.plot(y=df[])
    plt.show()