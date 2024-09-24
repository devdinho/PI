import numpy as np
import cv2

def rotulacao(imagem_binaria):
	altura, largura = imagem_binaria.shape
	rotulos = np.zeros_like(imagem_binaria, dtype=np.int32)
	r = 1
	equivalencias = {}
	
	for i in range(altura):
		for j in range(largura):
			if imagem_binaria[i, j] == 1:
				vizinho_esquerda = rotulos[i, j - 1] if j > 0 else 0
				vizinho_acima = rotulos[i - 1, j] if i > 0 else 0
				
				if vizinho_esquerda == 0 and vizinho_acima == 0:
					rotulos[i, j] = r
					r += 1
				elif vizinho_esquerda != 0 and vizinho_acima == 0:
					rotulos[i, j] = vizinho_esquerda
				elif vizinho_esquerda == 0 and vizinho_acima != 0:
					rotulos[i, j] = vizinho_acima
				else:
					menor_rotulo = min(vizinho_esquerda, vizinho_acima)
					maior_rotulo = max(vizinho_esquerda, vizinho_acima)
					rotulos[i, j] = menor_rotulo
					if maior_rotulo != menor_rotulo:
						if maior_rotulo not in equivalencias:
							equivalencias[maior_rotulo] = menor_rotulo
						else:
							equivalencias[maior_rotulo] = min(equivalencias[maior_rotulo], menor_rotulo)
	
	for i in range(altura):
		for j in range(largura):
			if rotulos[i, j] in equivalencias:
				rotulos[i, j] = equivalencias[rotulos[i, j]]
	
	return rotulos

imagem_binaria = np.array([
	[0, 0, 0, 1, 1, 0],
	[0, 1, 1, 1, 0, 0],
	[0, 1, 1, 0, 0, 1],
	[0, 0, 0, 1, 1, 1],
	[1, 1, 0, 0, 0, 0]
], dtype=np.uint8)

rotulos = rotulacao(imagem_binaria)

print("Imagem binária:")
print(imagem_binaria)
print("\nImagem rotulada:")
print(rotulos)