import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img1 = mpimg.imread('img/tc.png')


def get_distance(v, w=[1/3, 1/3, 1/3]): #default deger !!!!
    a,b,c = v[0], v[1], v[2]
    w1, w2, w3 = w[0], w[1], w[2]
    d = ((a**2)*w1 + (b**2)*w2 + (c**2)*w3)**0.5
    return d#((a*w1)**2 + (b*w2)**2 + (c*w3)**2)**(0.5)


def convert_rgb_to_gray_level(im_1):#renkliyi griye çevirme
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2 = np.zeros((m,n)) # boyutu belirttik yeni resmin
    for i in range(m):
        for j in range(n):
            im_2[i,j] = get_distance(im_1[i,j,:])
    return im_2


def convert_gray_level_to_BW(im_gray_level): #grileveli siyah beyaz yapma
    m=im_gray_level.shape[0]
    n=im_gray_level.shape[1]
    im_bw = np.zeros((m,n)) # boyutu belirttik yeni resmin
    for i in range(m):
        for j in range(n):
            if im_gray_level[i,j]>120:
                im_bw[i,j] =1
            else:
                im_bw[i,j]=0
    return im_bw

image_gl = convert_rgb_to_gray_level(img1)
img = convert_gray_level_to_BW(image_gl)

def piksel_compare_1(x, y):
    a =  ((image[x-1, y] == 0) and (image[x+1, y] == 0) and (image[x, y-1] == 0) and (image[x, y+1] == 1))
    b = ((image[x - 1, y] == 0) and (image[x + 1, y] == 0) and (image[x, y - 1] == 1) and (image[x, y + 1] == 0))
    c = ((image[x - 1, y]== 0) and (image[x + 1, y] == 1) and (image[x, y - 1] == 0 )and (image[x, y + 1] == 0))
    d = ((image[x - 1, y] == 1) and (image[x + 1, y] == 0) and (image[x, y - 1] == 0) and (image[x, y + 1] == 0))
    if a or b or c or d:
        return True
    else:
        return False


def piksel_compare_2(x, y):
    a = image[x - 1, y] == 1 and image[x + 1, y] == 1 and image[x, y - 1] == 1 and image[x, y + 1] == 0
    b = image[x - 1, y] == 1 and image[x + 1, y] == 1 and image[x, y - 1] == 0 and image[x, y + 1] == 1
    c = image[x - 1, y] == 1 and image[x + 1, y] == 0 and image[x, y - 1] == 1 and image[x, y + 1] == 1
    d = image[x - 1, y] == 0 and image[x + 1, y] == 1 and image[x, y - 1] == 1 and image[x, y + 1] == 1
    if a or b or c or d:
        return True
    else:
        return False


def img_komsu_bul(resim):
    sonuc = [0,0]
    m=im_1.shape[0]
    n=im_1.shape[1]
    for i in range(1, m-1):
        for j in range(1, n-1):
            if (piksel_compare_1(resim[i-1:i+1, j-1:j+1])):
                sonuc[0] += 1
            elif(piksel_compare_2(resim[i-1:i+1, j-1:j+1])):
                sonuc[1] += 1

    return sonuc
