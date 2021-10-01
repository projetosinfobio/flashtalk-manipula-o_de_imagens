# Bibliotecas
import cv2
import numpy as np

# Lendo uma imagem
imagem = cv2.imread('ej.jpeg')
cv2.imshow('EJ', imagem)

# Imagem em escala de cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cinza', cinza)

# Borrar a imagem
borrar = cv2.GaussianBlur(cinza, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', borrar)

# Fundo preto
preto = np.zeros(imagem.shape)
cv2.imshow('Blank', preto)

# Detecção da borda
canny = cv2.Canny(imagem, 125, 175)
cv2.imshow('Bordas', canny)

# Convertendo uma imagem em RGB para HSV
img_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img_hsv)
cv2.imshow('H', h)
cv2.imshow('S', s)
cv2.imshow('V', v)

# Detectando Cores
img = cv2.imread('formas.png')
cv2.imshow('image', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

faixa_inferior = np.array([159, 50, 70]) # Vermelho
faixa_superior = np.array([180, 255, 255])

# faixa_inferior = np.array([90, 50, 70]) # Azul
# faixa_superior = np.array([128, 255, 255])

# faixa_inferior = np.array([25,50,50]) # Amarelo
# faixa_superior = np.array([32,255,255])

# faixa_inferior = np.array([36, 50, 70]) # Verde
# faixa_superior = np.array([89, 255, 255])

mascara = cv2.inRange(hsv, faixa_inferior, faixa_superior)
 
cv2.imshow('image', img)
cv2.imshow('mask', mascara)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Preto:
    faixa_inferior = np.array([0, 0, 0])
    faixa_superior = np.array([180, 255, 30])
Branco:
    faixa_inferior = np.array([0, 0, 231])
    faixa_superior = np.array([180, 18, 255])
Vermelho:
    faixa_inferior = np.array([159, 50, 70])
    faixa_superior = np.array([180, 255, 255])
Verde:
    faixa_inferior = np.array([36, 50, 70])
    faixa_superior = np.array([89, 255, 255])
Azul:
    faixa_inferior = np.array([90, 50, 70])
    faixa_superior = np.array([128, 255, 255])
Amarelo:
    faixa_inferior = np.array([25, 50, 70])
    faixa_superior = np.array([35, 255, 255])
Roxo:
    faixa_inferior = np.array([129, 50, 70])
    faixa_superior = np.array([158, 255, 255])
Laranja:
    faixa_inferior = np.array([24, 255, 255])
    faixa_superior = np.array([10, 50, 70])
Cinza:
    faixa_inferior = np.array([180, 18, 230])
    faixa_superior = np.array([0, 0, 40])

'''