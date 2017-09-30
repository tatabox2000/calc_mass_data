import plotly.graph_objs as go
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import os
import glob
import peakutils

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
    name = name.replace("TXT", "")
    name = name.replace("..", "")
    total_data = df.sum(axis=1)
    data = go.Scatter(
        x=df.index,
        # y = df[name],
        y=total_data,
        name=name,
        line=dict(
            width=2)
    )
    sig_peaks = peakutils.indexes(total_data, thres=0.003,min_dist=10)
    peaks_x = np.round(df.index.values[sig_peaks],2).tolist()
    peaks_y = total_data.values[sig_peaks].tolist()

    trace = go.Scatter(
        x= peaks_x,
        y = peaks_y,
        #y=[total_data.iloc[j] for j in sig_peaks ],
        mode='markers+text',
        text = peaks_x,
        #text=[str(i) for i in peaks_x],
        name = 'Peak',
        textposition='top',
        textfont=dict(
            size=15
        ),
        marker=dict(
            size=4,
            color='rgb(100,0,255)',
            symbol=6
        ),
    )
    all_data.append(data)
    all_data.append(trace)
    all_name.append(name)
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
    if n == 0:
        #pass
        sep_data.append(data)
    elif n ==1:
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
        legend=dict(
            x=0.7,
            y=1,
            #orientation="h",
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=20,
                color='#000'
            ),
            # bgcolor='#E2E2E2',
            # bordercolor='#FFFFFF',
            # borderwidth=2
        )

    )
   # fig = dict(data=[sep_result], layout=layout)
    fig = dict(data=sep_data, layout=layout)
    plot(fig, filename= sep_name + '1.html',show_link=False)