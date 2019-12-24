# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 2019

@author: User + Chi-Kang
"""
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

ATOM_NUMBER = 92482
#ATOM_NUMBER = 482

def ReadEnergyData(filename):
    print('./%s' %filename)
    
    f = open('./%s' %filename, 'r')
    
    edata = []
    for line in f:
        if 'ITEM: ATOMS id c_1 c_2 ' in line: 
            for i, line in enumerate(f):
                edata.append([float(cell) for cell in line.split()])
                if i > ATOM_NUMBER:
                    break
    f.close()
    edata = sorted(edata, key=lambda edata: edata[0])
    return edata

def ReadAtomLocal(filename):
    print('./%s' %filename)
    
    f = open('./%s' %filename, 'r')
    atomlocal=[]
    for line in f:
        if 'Atoms' in line:
            for i, line in enumerate(f):
                atomlocal.append([float(cell) for cell in line.split()])
                if i > ATOM_NUMBER:
                    break
    f.close()

    del atomlocal[0]
    return atomlocal

atomlocal = ReadAtomLocal('92482.tect')
edata     = ReadEnergyData('pe0129331.80.5_Kb20000_Ka500_step60000')


# list to array
atomlocal = np.array(atomlocal)
edata = np.array(edata)

atomlocal = atomlocal[:, 3:] # 去掉 ID, 不重要, 不重要
print('shape of atomlocal:', atomlocal.shape)

edata = edata[:ATOM_NUMBER+1, 1:] # 去掉 ID
print('shape of edata:', edata.shape)

fig = plt.figure(figsize=(6,6))

ax = Axes3D(fig) # Method 1
# ax = fig.add_subplot(111, projection='3d') # Method 2

# 3D scatter plot
x = atomlocal[:, 0]
y = atomlocal[:, 1]
z = atomlocal[:, 2]
e = edata[:, 0] + edata[:, 1]

ax.scatter(x, y, z, c=e, marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()


# save figure
#fig.savefig('output', transparent=True, dpi=100, pad_inches = 0)
