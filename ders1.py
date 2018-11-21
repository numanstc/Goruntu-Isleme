#max min Fonksiyonu

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


img = mpimg.imread('img/agac.jpg')

def myFunction(my_img):
    print ("Eksen Sayısı: ", my_img.ndim)
    print ("Eksen Değeri: ", my_img.shape)
    print ("En Küçük Kırmızı Renk Değeri: ", np.min(my_img[:,:,0]))
    print ("En Büyük Kırmızı Renk Değeri: ", np.max(my_img[:,:,0]))
    print ("En Küçük Yeşil Renk Değeri: ", np.min(my_img[:,:,1]))
    print ("En Büyük Yeşil Renk Değeri: ", np.max(my_img[:,:,1]))
    print ("En Küçük Mavi Renk Değeri: ", np.min(my_img[:,:,2]))
    print ("En Büyük Mavi Renk Değeri: ", np.max(my_img[:,:,2]))

myFunction(img)
