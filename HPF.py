import numpy as np #import liblary openCV
import cv2
from scipy import ndimage as im

scr = cv2.imread('HIMPROTE.png')
#deklarasi file sumber gambar
gray= cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)
#konvert file sumber (RGB) ke grayscale
data= np.array(gray, dtype=float)
#pemanggilan perintah matriks dari kernel

kernel = np.array([[-30, 7, -7],
                   [ 2,  0, 30],
                   [ -3, 1, -1]])
#data matriks

HPF = im.convolve(data, kernel)
#pemrosesan High Pass Filter dengan cara
#mengkonvolusi matrik gray dengan kernel 3x3

cv2.imshow('Gambar sumber',scr)
#menampilkan gambar asli
cv2.imshow('hasil High Pass Filter',HPF)
#menampilkan gambar hasil Low Pass Filter
cv2.waitKey()
#menunggu input dari keyboard
cv2.destroyAllWindows()
#lalu tutup semua windows jika ada keyboard yang ditekan