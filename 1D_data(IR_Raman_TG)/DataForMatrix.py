import numpy as np
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import plotly.graph_objs as go
import plotly.figure_factory as ff
import glob
import os
import seaborn as sns
from IPython.display import display,HTML
import pylab as plt
#import cufflinks as cf
#cf.go_offline()

DIR = "C:\\Users\\admin\\OneDrive\\IR_Raman_TG\\IR\\"
DIR = "C:\\Users\\tatab\\OneDrive\\IR_Raman_TG\\Raman\\"
os.chdir(DIR)

file_names = glob.glob('./*CSV')
left,right = 0,0
for num,name in enumerate(file_names):
    df = pd.read_csv(name)
    name = name.replace(".\\", "")
    name = name.replace(".CSV", "")
    df.columns = ['cm-1', name]
    if num == 0:
        left = df
    else:
        right = df
        left = pd.merge(left,right,how="inner")
#save
#left = left.T
left.to_csv('.\\result\\All_Ramman.csv')
left = left.set_index('cm-1')
left = left.iloc[:]
#print(left)

#scatter matrix
#fig = ff.create_scatterplotmatrix(left,diag='histogram',height=900, width=900,)
#plot(fig,filename='Diagonal_Subplots.html')

#heat map
#"""
sns.set_context("notebook", font_scale=1.3, rc={"lines.linewidth": 2.5})
sns.heatmap(left.corr(),annot=True, fmt='1.2f', cmap='Blues',vmax= 1.0,vmin=0.5)
plt.yticks(rotation=0)
plt.xticks(rotation=30)
plt.show()
#"""
