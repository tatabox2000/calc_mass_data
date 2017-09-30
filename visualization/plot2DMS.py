import plotly.graph_objs as go
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import os
import glob

title='PY-GC-MS'

if title == 'PY-GC-MS':
    DIR = 'C:\\Users\\tatab\\OneDrive\\Data\\AIAEXPRT.AIA\\TIC_data\\'
    DIR = 'C:\\Users\\tatab\\OneDrive\\waters\\test\\others'
    xname = 'time'
    yname = 'count'
    autorange = True
os.chdir(DIR)
file_names = glob.glob('./*CSV')

all_data = []
all_name= []
for n ,name in enumerate(file_names):
    print(name)
    df = pd.read_csv(name,header=0,index_col='time')
    df2 = df.sum(axis=1)
    name = name.replace(".\\", "")
    name = name.replace("csv", "")
    name = name.replace("CDF", "")
    name = name.replace("..", "")

    data =go.Scatter(
        x = df.index,
        #y = df[name],
        y=df.sum(axis=1),
        name = name,
        line = dict(
            width = 2)
    )
    all_data.append(data)
    all_name.append(name)

#subplot
"""
fig = tools.make_subplots(rows=2, cols=2, subplot_titles=(u'機械処理(大王)',u'機械処理(SUGINO)','Reference', 'TEMPO酸化'),)
xname='time'
yname='count'
autorange = 'autorange'
fig['layout'] ['xaxis1'].update(title=xname,autorange=autorange)
fig['layout'] ['xaxis2'].update(title=xname,autorange=autorange)
fig['layout'] ['xaxis3'].update(title=xname,autorange=autorange)
fig['layout'] ['xaxis4'].update(title=xname,autorange=autorange)
fig['layout'] ['yaxis1'].update(title=yname)
fig['layout'] ['yaxis2'].update(title=yname)
fig['layout'] ['yaxis3'].update(title=yname)
fig['layout'] ['yaxis4'].update(title=yname)
for i in np.arange(0,4,1):
    fig['layout']['annotations'][i]['font'].update(size=20)
fig['layout'].update(height=700, width=900, title=title + ' Charts')
for n,trace in enumerate(all_data):
    if n < 3:
        fig.append_trace(trace, 1, 1)
    elif n < 7 :
        fig.append_trace(trace, 1, 2)
    elif n < 9 :
        fig.append_trace(trace, 2, 1)
    elif n < 11:
        fig.append_trace(trace, 2, 2)
#all plot
"""
sep_data = []
for n,data  in enumerate(all_data):
    if n == 2:
        #pass
        sep_data.append(data)
    elif n ==4:
        #pass
        sep_data.append(data)
    elif n == 8:
        #pass
        sep_data.append(data)
    elif n==9:
        #pass
        sep_data.append(data)


#fig = dict(data=sep_data, layout=layout)
for sep_result,sep_name in zip(all_data, all_name):
    layout = dict(
        # title = title +' Charts',
        title=sep_name +'Chart',
        xaxis=dict(title=xname, autorange=autorange),
        yaxis=dict(title=yname),
    )
    fig = dict(data=[sep_result], layout=layout)

    plot(fig, filename= sep_name + '1.html',show_link=False)