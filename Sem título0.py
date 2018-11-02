import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
import pylab as pl
import random
from sklearn import ensemble
import numpy as np
import cv2

def imglist(fruit_name):
    fruit_image_list = []
    for c in range(350):
        img = cv2.imread('fruits/fruits-360/Training/{0}/{1}_100.jpg'.format(fruit_name,c),1)
        if type(img) != type(None):
            fruit_image_list.append(img)
    for c in range(350):
        img = cv2.imread('fruits/fruits-360/Training/{0}/r_{1}_100.jpg'.format(fruit_name,c),1)
        if type(img) != type(None):
            fruit_image_list.append(img)
    for c in range(350):
        img = cv2.imread('fruits/fruits-360/Training/{0}/r2_{1}_100.jpg'.format(fruit_name,c),1)
        if type(img) != type(None):
            fruit_image_list.append(img)
    return fruit_image_list


lemon = imglist("Lemon")


print(len(lemon))

img = lemon[345]
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
    
