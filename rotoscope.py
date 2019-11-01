########################################################################
# Projeto           : Desafio Senai: Filtro Pencil Draw
#
# Nome do programa  : rotoscope.py
#
# Autor             : Alison Morais, Diogo Lima, Edilton Junior
#
# Data de criacao   : 31-10-2019
#
# Funcionamento     : Le um arquivo de imagem passado como parametro e o transforma em lineart atraves do tramanho do kernel informado.
#                     A seguir, usa uma mescla opaca para dar a imagem uma coloracao que lembra o efeito de rotoscopia.
#                     Argumentos: 0-Caminho da imagem, 1-Kernel (sugerido: entre 5 e 21), 2- Peso da lineart (sugerido: entre 0 e 1), 
# 					  3- Peso das cores originais (sugerido: entre 0 e 1)
#
# Hist. de Revisao  :
#
# Data        Author      Ref    Revisao
# 31-10-2019  diogo       1      Codigo finalizado
# 01-11-2019  diogo       2      Codigo passou a aceitar argumentos de entrada
########################################################################

import cv2
import numpy as np
import sys


def criaLineart(img):

# Converte a imagem para escala de cinza
	grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Inverte os pixels da imagem
	inverted = cv2.bitwise_not(grayscale)
# Aplica gaussian blur na imagem invertida
	gaussinv = cv2.GaussianBlur(inverted,(int(sys.argv[2]),int(sys.argv[2])),cv2.BORDER_DEFAULT)
# Color blend nas duas imagens
	lineart = cv2.divide(grayscale, cv2.bitwise_not(gaussinv), scale = 256.0)
# Converte a lineart para 3 canais
	lineart3ch = cv2.cvtColor(lineart,cv2.COLOR_GRAY2BGR)

	cv2.imwrite('lineart_rotoscope.jpg', lineart3ch)
	return lineart3ch

def efeitoRotoscope(img, lineart):
# Cria o efeito de rotoscope
	rotoscope = cv2.addWeighted(lineart,float(sys.argv[3]),img,float(sys.argv[4]),0)

	cv2.imwrite('rotoscope.jpg', rotoscope)
	return rotoscope


def concatenaExibe(img1, img2, showName):
# Une duas imagens horizontalmente
	concat = np.concatenate((img1, img2), axis=1)
	cv2.imshow(showName, concat)

	return concat

########################### CODIGO PRINCIPAL ##########################

# Lê a imagem dos argumentos
img = cv2.imread(sys.argv[1])

# Aplica os filtros
lineart = criaLineart(img)
rotoscope = efeitoRotoscope(img, lineart)

# Exibe os resultados
concatenaExibe(img, lineart, "Lineart")
concatenaExibe(img, rotoscope, "Rotoscope")

cv2.waitKey(0)

############################ FIM DO CODIGO ############################

