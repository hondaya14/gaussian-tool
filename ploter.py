import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X, Y, Z, V = [], [], [], []
while True:
    try:
        x, y, z, value = list(map(float, input().split()))
        X.append(x)
        Y.append(y)
        Z.append(z)
        V.append(value)
    except EOFError:
        break

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)
V = np.array(V)

plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'Times New Roman'

fig = plt.figure()
ax1 = Axes3D(fig)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

ax1.scatter(X, Y, V)
plt.legend()

plt.show()
plt.close()
