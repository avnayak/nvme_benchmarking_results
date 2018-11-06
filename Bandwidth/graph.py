import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

data = np.loadtxt('32k.text',delimiter='\t')
r = data[:,0]
r1 = data[:,1]
r2 = data[:,2]
r3 = data[:,3]
r4 = data[:,4] 
fig = plt.figure()
fig.patch.set_facecolor('white')
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 50,
        }
plt.xlabel('Run Time',fontdict=font)
plt.ylabel('IOPS',fontdict=font)
rr = mpatches.Patch(color='green', label='random read')
sqr = mpatches.Patch(color='orange', label='sequential read')
sqw = mpatches.Patch(color='purple', label='sequential write')
rw = mpatches.Patch(color='yellow', label='random write')
rrw = mpatches.Patch(color='blue', label='random read write')
plt.legend(handles=[rr,sqr,sqw,rw,rrw])
plt.plot(r,linestyle='-',color='green',linewidth=6)
plt.plot(r1,linestyle='-',color='orange',linewidth=6)
plt.plot(r2,linestyle='-',color='purple',linewidth=6)
plt.plot(r3,linestyle='-',color='yellow',linewidth=6)
plt.plot(r4,linestyle='-',color='blue',linewidth=6)
plt.plot(r,'ro')
plt.plot(r1,'ro')
plt.plot(r2,'ro')
plt.plot(r3,'ro')
plt.plot(r4,'ro')
plt.show()
