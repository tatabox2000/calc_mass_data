import numpy as np
import pylab as plt

x = np.arange(1,1000,1)
y = np.sin(x/(10*np.pi))
y_diff = np.diff(y)

bool_plus = y_diff > 0
bool_zero = y_diff == 0
bool_minus = y_diff <0
bool_minus_chack = np.roll(bool_minus,-1)

bool_chack = np.logical_and(bool_plus,bool_minus_chack)
bool_chack = np.logical_or(bool_chack , bool_zero)

print(np.where(bool_chack==True))
#print(bool_chack)
#y_diff = np.append(y_diff,1)
y_diff[0]=0


plt.plot(x,y)
plt.show()