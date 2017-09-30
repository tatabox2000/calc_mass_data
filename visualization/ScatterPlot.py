import plotly.graph_objs as go
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import os
import glob

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
    DIR = 'C:\\Users\\tatab\\OneDrive\\Data\\AIAEXPRT.AIA\\GCMS_TIC'
    xname = 'time'
    yname = 'count'
    autorange = True

elif title == 'PY-GC-MS':
    DIR = 'C:\\Users\\admin\\OneDrive\\Data\\AIAEXPRT.AIA\\'
    xname = 'time'
    yname = 'count'
    autorange = True
    #DIR = 'C:\\Users\\admin\\OneDrive\\Data\\AIAEXPRT.AIA\\'

os.chdir(DIR)

file_names = glob.glob('./*CSV')
left,right = 0,0
for num,name in enumerate(file_names):
    print(name)

    df = pd.read_csv(name,header=4)
    name = name.replace(".\\", "")
    name = name.replace(".CSV", "")

    df.columns = [yname, name]
    if num == 0:
        left = df
    else:
        right = df
        left = pd.merge(left,right,how="inner")
df = left.set_index(yname)

all_data = []
for n ,name in enumerate( df.columns.values):
    data =go.Scatter(
        x = df.index.values,
        y = df[name],
        #y=df.values,
        #y=df.sum(axis=1),
        name = name,
        line = dict(
            width = 2)
    )
    all_data.append(data)

#subplot
#"""
#fig = tools.make_subplots(rows=2, cols=3, subplot_titles=(u'機械処理(大王)',u'機械処理(SUGINO)','Reference', 'TEMPO酸化'),)
fig = tools.make_subplots(rows=2, cols=3, subplot_titles=(u'ポリエチレン',u'ラテックス','','8:2','5:5','3:7'),)


fig['layout'] ['xaxis1'].update(title=xname,autorange=autorange)
fig['layout'] ['xaxis2'].update(title=xname,autorange=autorange)
fig['layout'] ['xaxis4'].update(title=xname,autorange=autorange)
fig['layout'] ['xaxis5'].update(title=xname,autorange=autorange)
fig['layout'] ['xaxis6'].update(title=xname,autorange=autorange)

fig['layout'] ['yaxis1'].update(title=yname)
fig['layout'] ['yaxis2'].update(title=yname)
fig['layout'] ['yaxis4'].update(title=yname)
fig['layout'] ['yaxis5'].update(title=yname)
fig['layout'] ['yaxis6'].update(title=yname)

for i in np.arange(0,4,1):
    fig['layout']['annotations'][i]['font'].update(size=20)
fig['layout'].update(height=700, width=900, title=title + ' Charts')
for n,trace in enumerate(all_data):
    if n < 1:
        fig.append_trace(trace, 1,2)
    elif n < 2 :
        fig.append_trace(trace, 2, 3)
    elif n < 3 :
        fig.append_trace(trace, 2, 2)
    elif n < 4:
        fig.append_trace(trace, 2, 1)
    elif n < 5:
        fig.append_trace(trace, 1, 1)
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
"""
layout = dict(title = title +' Charts',
              xaxis = dict(title = xname, autorange = autorange),
              yaxis = dict(title = yname),
              )
#fig = dict(data=sep_data, layout=layout)
#fig = dict(data=all_data, layout=layout)

plot(fig, filename= title + '1.html',show_link=False)
