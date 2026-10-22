import numpy as np
# Emily Barrza NC 0025
n0025= np.array([13, 1, 20, 11, 6])
print(n0025)
print(n0025[0])
print(n0025[3])
print(n0025[-1])
print(n0025[-2])
print("------------------------------------")
n0025= np.array([
    [13, 1, 20],
    [11, 6, 8]
])
print(n0025)
print(n0025[0,0])
print(n0025[1,2])
print(n0025[-1,-1])
print(n0025[-2,-2])
print("------------------------------------")
# 3D array 2x(2x3)
n0025= np.array([
[
    [13, 1, 20],
    [11, 6, 8]
],
[
    [70,80,90],
    [108,118,120]
    ]
])
print(n0025)
print(n0025[0, 0, 0])
print(n0025[1, 1, 2])
print(n0025[-1, -1, -2])
print("Emily Barrza NC 0025")