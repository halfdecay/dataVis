import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D

filename = '/home/dsukol/Documents/prog/goniophotometr/build-Goniophotometr-Desktop_Qt_5_12_5_GCC_64bit-Debug/pointdata.xyz'

with open(filename) as f:
    mylist = f.read().splitlines()

# kapa =f.readlines()
# # datapoints = kapa.sort("\n")
print(type(mylist))
x = np.array([])
y = np.array([])
z = np.array([])
lenlist = len(mylist)

for i in mylist:
    # print(float(i.split(" ")[0]))
    x=np.append (x, float(i.split(" ")[0]))
    y=np.append(y, float(i.split(" ")[1]))
    z=np.append(z,float(i.split(" ")[2]))

    # x =mylist[i].split(" ")[0]
    # y = mylist[i].split(" ")[1]
    # z = mylist[i].split(" ")[2]

print(x)
points = lenlist
data = np.zeros([points,3])

# x = np.random.rand(points)*100
# y = np.random.rand(points)*100
# z = np.random.rand(points)*100
# z = np.sinc((x-20)/100*3.14) + np.sinc((y-50)/100*3.14)

# for i in mylist:
#     np.append (x, i.split(" ")[0])
#     np.append(y, i.split(" ")[1])
#     np.append(z, i.split(" ")[2])

    # points = 500
    # data = np.zeros([points,3])
    # x = np.random.rand(points)*100
    # y = np.random.rand(points)*100
    # z = np.sinc((x-20)/100*3.14) + np.sinc((y-50)/100*3.14)


triang = mtri.Triangulation(x, y)
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_trisurf(triang, z, cmap='jet')
ax.scatter(x,y,z, marker='.', s=10, c="black", alpha=0.5)
ax.view_init(elev=60, azim=-45)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()