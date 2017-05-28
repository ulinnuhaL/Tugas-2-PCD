import numpy as np #import liblary openCV
import cv2

scr = cv2.imread('HIMPROTE.png')
#deklarasi file sumber gambar
LPF = cv2.filter2D(scr,-1,np.ones((15,15),np.float32)/255)
#pemrosesan Low Pass Filter dengan mengisi digit satu(np.ones)
#dengan kernel 15x15
#>kernel>pula tingkat filter rendahnya (semakin blur gambarnya)
cv2.imshow('Gambar sumber',scr)
#menampilkan gambar asli
cv2.imshow('hasil Low Pass Filter',LPF)
#menampilkan gambar hasil Low Pass Filter
cv2.waitKey()
#menunggu input dari keyboard
cv2.destroyAllWindows()
#lalu tutup semua windows jika ada keyboard yang ditekan