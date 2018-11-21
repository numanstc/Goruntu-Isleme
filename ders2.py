# Tersini alma

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('img/agac.jpg')

def myHistogram(my_img):
    his_R = {}
    for i in range(my_img.shape[0]):
        for j in range(my_img.shape[1]):
            if (my_img[i, j, 0] in his_R.keys()):
                his_R[my_img[i, j, 0]] += 1
            else:
                his_R[my_img[i, j, 0]] = 1

    his_G = {}
    for i in range(my_img.shape[0]):
        for j in range(my_img.shape[1]):
            if (my_img[i, j, 1] in his_G.keys()):
                his_G[my_img[i, j, 1]] += 1
            else:
                his_G[my_img[i, j, 1]] = 1

    his_B = {}
    for i in range(my_img.shape[0]):
        for j in range(my_img.shape[1]):
            if (my_img[i, j, 2] in his_B.keys()):
                his_B[my_img[i, j, 2]] += 1
            else:
                his_B[my_img[i, j, 2]] = 1
    return (his_R, his_G, his_B)

my_histogram = myHistogram(img)

x = []
y = []
for i in my_histogram[0].keys():
    x.append(i)
    y.append(my_histogram[0][i])
plt.subplot(1,3,1),plt.plot(x,y)

x = []
y = []
for i in my_histogram[1].keys():
    x.append(i)
    y.append(my_histogram[1][i])
plt.subplot(1,3,2),plt.plot(x,y)

x = []
y = []
for i in my_histogram[2].keys():
    x.append(i)
    y.append(my_histogram[2][i])
plt.subplot(1,3,3),plt.plot(x,y)
