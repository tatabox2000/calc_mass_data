from scipy import signal
import  numpy as np
import  pylab as plt
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

