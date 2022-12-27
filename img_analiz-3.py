import cv2
import numpy as np


# abstraindo a imagem

img = cv2.imread("img/card01.bmp",(0))

__, thresh = cv2.threshold(img,127 ,255,cv2.THRESH_BINARY)

thresh_l1 = img[00:20, 0:800]
thresh_c1 = img[00:800, 0:40]


modo = cv2.RETR_TREE;
metodo = cv2.CHAIN_APPROX_SIMPLE;
contorno, hieraquia = cv2.findContours(thresh, modo , metodo)
full_card = len(contorno) -1
print(" Total de retângulos: ",full_card)


linha, hieraquia = cv2.findContours(thresh_l1, modo , metodo)
count_line = len(linha) -1
print(" Total de retângulos na 1ª linha: ",count_line)


coluna, hieraquia = cv2.findContours(thresh_c1, modo , metodo)
count_col= len(coluna) -1
print(" Total de retângulos na 1ª coluna: ",count_col)

#opção para visualizar os card's

cv2.imshow("card-original", img)
cv2.imshow ("thr_linha", thresh_l1)
cv2.imshow("thr",thresh_c1)

cv2.waitKey(0)
cv2.destroyAllWindows()