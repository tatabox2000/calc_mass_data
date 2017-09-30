import plotly.graph_objs as go
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import os
import glob
import csv
#title = "IR"
title='Raman'
title='TG'
#DIR = "C:\\Users\\tatab\\OneDrive\\IR_Raman\\IR\\"
#DIR = "C:\\Users\\tatab\\OneDrive\\IR_Raman\\Raman\\"
DIR = "C:\\Users\\admin\\OneDrive\\IR_Raman_TG\\TG\\"

os.chdir(DIR)

file_names = glob.glob('./*csv')
left,right = 0,0
column_names = ['time','temp','Weight','B Flow','S Flow','dx']
all_data = []
for num,file_name in enumerate(file_names):
    print(file_names)
    df = pd.read_csv(file_name,skiprows=86,encoding='CP932',names = column_names,index_col='temp')

    file_name = file_name.replace(".\\", "")
    file_name = file_name.replace(".csv", "")


    for n, name in enumerate(df.columns.values):
        if name == 'time' or name == 'B Flow' or name == 'S Flow':
            pass
            #"""
        elif name == 'Weight':
            if df[name].min() < 0:
                df['Weight[%]'] = (df[name]- df[name].min())/(df[name].max()-df[name].min()) *100
                data = go.Scatter(
                    x=df.index.values,
                    y=df['Weight[%]'],
                    name=name+file_name,
                    line=dict(
                        width=2)
                )
                all_data.append(data)
            else:
                df['Weight[%]'] = df[name]  / df[name].max() * 100
                data = go.Scatter(
                    x=df.index.values,
                    y=df['Weight[%]'],
                    name=name+file_name,
                    line=dict(
                        width=2)
                )
                all_data.append(data)
                #"""
        elif name == 'dx':
            data = go.Scatter(
                x=df.index.values,
                y=df[name]/df[name].sum(),
                name=name+file_name,
                yaxis='y2',
                line=dict(
                    width=2)
            )
            all_data.append(data)
            #"""
print(all_data[5])
layout = dict(title=title + ' Charts',
                xaxis=dict(title='Temp'),
                yaxis=dict(title='%',range=[0,100]),
                yaxis2=dict(title='Ratio',overlaying='y',side = 'right',range=[0,0.002]),
                )
#subplot
"""
fig = tools.make_subplots(rows=2, cols=2, subplot_titles=(u'機械処理(大王)',u'機械処理(SUGINO)',' ', 'TEMPO酸化'),)

fig['layout'] ['xaxis1'].update(title='temp')
fig['layout'] ['xaxis2'].update(title='temp')
#fig['layout'] ['xaxis3'].update(title='temp')
fig['layout'] ['xaxis4'].update(title='temp')
fig['layout'] ['yaxis1'].update(title='%')
fig['layout'] ['yaxis2'].update(title='%')
#fig['layout'] ['yaxis3'].update(title='%')
fig['layout'] ['yaxis4'].update(title='%')
for i in np.arange(0,4,1):
    fig['layout']['annotations'][i]['font'].update(size=20)
fig['layout'].update(height=700, width=900, title=title + ' Charts')
for n,trace in enumerate(all_data):
    if n < 3:
        fig.append_trace(trace, 1, 1)
    elif n < 8 :
        fig.append_trace(trace, 1, 2)
    #elif n < 9 :
        #pass
        #fig.append_trace(trace, 2, 1)
    elif n < 10:
        fig.append_trace(trace, 2, 2)
        """

#all plot
fig = dict(data=all_data[0:1], layout=layout)
plot(fig, filename= file_name + '.html',show_link=False)

