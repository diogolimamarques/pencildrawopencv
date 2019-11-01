########################################################################
# Projeto           : Desafio Senai: Filtro Pencil Draw
#
# Nome do programa  : pencilsketch.py
#
# Autor             : Alison Morais, Diogo Lima, Edilton Junior
#
# Data de criacao   : 30-10-2019
#
# Funcionamento     : Le um arquivo de imagem com nome 'ss.jpg' na pasta raiz. Usa diversas formas de blur para gerar efeitos variados
#                     de pencil draw.
#                     Argumentos: Nenhum (Deve haver uma imagem com nome 'ss.jpg' na pasta raiz.)
#
# Hist. de Revisao  :
#
# Data        Author      Ref    Revisao
# 30-10-2019  edilton     1      Publicacao do Codigo
# 01-11-2019  diogo       2      Estruturacao dos Comentarios e Funcoes
########################################################################

import cv2
import numpy as np

kernelSize = 5

def converteGreyscale(img):
	pb = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	return pb

def negativaImagem(img):
	neg = cv2.bitwise_not(img)

	return neg

def blurHorizontal(img):
	global kernelSize

# Criando kernel horizontal para o motion blur com numpy 
	kernel_h = np.copy(np.zeros((kernelSize, kernelSize)))
# Adicionando 1´s nas matrizes
	kernel_h[int((kernelSize - 1)/2), :] = np.ones(kernelSize) 
# Normalizando e aplicando os filtros de embaçamento. 
	kernel_h /= kernelSize

	return cv2.filter2D(img, -1, kernel_h) 

def blurVertical(img):
	global kernelSize
# Criando kernel vertical para o motion blur com numpy 
	kernel_v = np.zeros((kernelSize, kernelSize))
# Adicionando 1´s nas matrizes
	kernel_v[:, int((kernelSize - 1)/2)] = np.ones(kernelSize) 
# Normalizando e aplicando os filtros de embaçamento. 
	kernel_v /= kernelSize

	return cv2.filter2D(img, -1, kernel_v)

def blurGaussian(img):
	return cv2.GaussianBlur(img,(5,5),7)

def blurMedian(img):
	return cv2.medianBlur(img,15)

def blurBilateral(img):
	return cv2.bilateralFilter(img,10,90,90)

def colorDodge(img, imgBlur):
# Divisão escalar para gerar o efeito pencil nas imagens

	result = cv2.divide(img, cv2.bitwise_not(imgBlur), scale = 256.0)

	return result

def bitAnd(img1, img2):
	return cv2.bitwise_and(img1,img2)


########################### CODIGO PRINCIPAL ##########################

# Le a imagem com o nome pre determinado

img = cv2.imread('ss.jpg')

# Converte para Greyscale e Inverte a imagem
pb = converteGreyscale(img)
neg = negativaImagem(pb)

# Aplica os blurs na imagem invertida
blurHori = blurHorizontal(neg)
blurVert = blurVertical(neg)
blurGaus = blurGaussian(neg)
blurMedi = blurMedian(neg)
blurBila = blurBilateral(neg)

# Divisão escalar para gerar o efeito pencil nas imagens

out1 = colorDodge(pb, blurHori)
out2 = colorDodge(pb, blurVert)
out3 = colorDodge(pb, blurGaus)
out4 = colorDodge(pb, blurMedi)
out5 = colorDodge(pb, blurBila)

# Aplicando algebra booleana na imagens geradas para criar um novo estilo

out6 = bitAnd(out2, out1)

# Salva e exibe os resultados

cv2.imshow("motion blur horizontal", out1)
cv2.imwrite('mbh.jpg', out1)

cv2.imshow("motion blur vertical", out2)
cv2.imwrite('mbv.jpg', out2)

cv2.imshow("Gaussian", out3)
cv2.imwrite('gauss.jpg', out3)

cv2.imshow("median", out4)
cv2.imwrite('median.jpg', out4)

cv2.imshow("bilateral", out5)
cv2.imwrite('bilat.jpg', out5)

cv2.waitKey(0)

# Exibe resultado da operacao de adicao bit a bit

cv2.imshow("bit_and", out6)
cv2.imwrite('bitand.jpg', out6)

cv2.waitKey(0)


############################ FIM DO CODIGO ############################
