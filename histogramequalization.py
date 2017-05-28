import numpy as np 
#import liblary numpy
import cv2
#import liblary openCV
from matplotlib import pyplot as plt
#import liblary pyplot, pemanggilan fungsi dengan "plt"
#untuk langsung plotting 2/ lebih histogram dalam satu window/ figure
scr = cv2.imread('HIMPROTE.png')
#deklarasi file sumber gambar
gray= cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)
#konvert file sumber (RGB) ke grayscale
equ = cv2.equalizeHist(gray)
cv2.imshow('Gambar sumber',scr)
#menampilkan gambar asli
cv2.imshow('hasil Histogram Equalization',equ)
#menampilkan gambar hasil Low Pass Filter
plt.figure('hasil Histogram Equalization')
#memunculkan 1 figure dengan nama 'hasil Histogram Equalization'
plt.subplot(2,1,1),plt.hist(gray.ravel(),256,[0,256]),plt.title('Histogram Awal')
#plotting histogram awal di urutan ke-1 dalam figure
plt.subplot(2,1,2),plt.hist(equ.ravel(),256,[0,256]), plt.title('Histogram Equalization')
#plotting histogram equalization di urutan ke-2 dalam figure
plt.show()
#memunculkan plot
cv2.waitKey()
#menunggu input dari keyboard
cv2.destroyAllWindows()
#lalu tutup semua windows jika ada keyboard yang ditekan