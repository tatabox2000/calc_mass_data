from scipy import signal
import  numpy as np
import  pylab as plt
import  peakutils
import plotly
plotly.offline.init_notebook_mode()
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
from plotly.graph_objs import *



t = np.linspace(0, 400, 400, endpoint=False)
#sig  = 2*np.cos(2 * np.pi * 7 * t) +np.sin( np.pi * t+np.pi*1/5)
n1= 40
sig1 = signal.gaussian(n1, std=5)*10
sig = np.zeros(400)

for i,n in enumerate([50,80,95,110,150]):
    sig_temp = np.zeros(400)
    if i == 0:
        i =0.5
    sig_temp[n-n1:n]  = sig1/i
    sig[n-n1:n] = sig[n-n1:n] + sig_temp[n-n1:n]
sig_peaks = peakutils.indexes(sig,thres=0.1)
print(sig_peaks)

trace = Scatter(
    x = t,
    y = sig,
    mode = 'lines',
)

trace2 = Scatter(
    x = sig_peaks,
    y = [sig[j]+0.3 for j in sig_peaks],
    mode = 'markers+text',
    text = [str(i) for i in sig_peaks],
    textposition='top',
    textfont= dict(
        size = 20
    ),
    marker=dict(
         size=10,
         color='rgb(100,0,255)',
        symbol=6
     ),
)

data = [trace,trace2]
plot(data,filename='result.html')

#sig[sig < 0 ] = 0
#sig[0:10 ] = 0
#sig[190:200]= 0

#widths = np.arange(1, 31)
widths = np.arange(1,31)
cwtmatr = signal.cwt(sig, signal.ricker, widths)
plt.plot(t,sig)
plt.show()

print(cwtmatr.shape)
plt.imshow(cwtmatr, extent=[0, 400, 1, 31], cmap='PRGn', aspect='auto',
vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
plt.show()

