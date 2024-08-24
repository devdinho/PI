import numpy as np
import cv2

def interpolacao_vizinho_mais_proximo(imagem, nova_largura, nova_altura):
    altura_original, largura_original = imagem.shape[:2]
    imagem_redimensionada = np.zeros((nova_altura, nova_largura, 3), dtype=np.uint8)

    for i in range(nova_altura):
        for j in range(nova_largura):
            # Encontrando o pixel mais próximo na imagem original
            x = int(j * (largura_original / nova_largura))
            y = int(i * (altura_original / nova_altura))
            imagem_redimensionada[i, j] = imagem[y, x]

    return imagem_redimensionada

def interpolacao_bilinear(imagem, nova_largura, nova_altura):
    altura_original, largura_original = imagem.shape[:2]
    imagem_redimensionada = np.zeros((nova_altura, nova_largura, 3), dtype=np.uint8)

    for i in range(nova_altura):
        for j in range(nova_largura):
            # Coordenadas reais na imagem original
            x = j * (largura_original / nova_largura)
            y = i * (altura_original / nova_altura)

            x_chao = int(np.floor(x))
            y_chao = int(np.floor(y))
            x_teto = min(x_chao + 1, largura_original - 1)
            y_teto = min(y_chao + 1, altura_original - 1)

            # Fatores de ponderação
            a = x - x_chao
            b = y - y_chao

            # Ponderar os 4 pixels vizinhos
            superior_esquerdo = imagem[y_chao, x_chao]
            superior_direito = imagem[y_chao, x_teto]
            inferior_esquerdo = imagem[y_teto, x_chao]
            inferior_direito = imagem[y_teto, x_teto]

            valor_pixel = (
                (1 - a) * (1 - b) * superior_esquerdo +
                a * (1 - b) * superior_direito +
                (1 - a) * b * inferior_esquerdo +
                a * b * inferior_direito
            )
            imagem_redimensionada[i, j] = valor_pixel

    return imagem_redimensionada

# Carregar imagem
imagem = cv2.imread('imagem.jpg')
altura, largura, canais = imagem.shape

# Redimensionar com vizinho mais próximo
imagem_redimensionada_vizinho_mais_proximo = interpolacao_vizinho_mais_proximo(imagem, largura*3, altura*3)
cv2.imwrite('imagem_redimensionada_vizinho_mais_proximo.jpg', imagem_redimensionada_vizinho_mais_proximo)

# Redimensionar com interpolação bilinear
imagem_redimensionada_bilinear = interpolacao_bilinear(imagem, largura*3, altura*3)
cv2.imwrite('imagem_redimensionada_bilinear.jpg', imagem_redimensionada_bilinear)
