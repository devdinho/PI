import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_mean_filter(image, kernel_size):
  
  if kernel_size % 2 == 0:
    raise ValueError("O tamanho do kernel deve ser ímpar.")

  pad_size = kernel_size // 2
  padded_image = cv2.copyMakeBorder(image, pad_size, pad_size, pad_size, pad_size, cv2.BORDER_REFLECT)

  filtered_image = np.zeros_like(image, dtype=np.uint8)

  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        
      roi = padded_image[i:i + kernel_size, j:j + kernel_size]
      
      filtered_image[i, j] = np.mean(roi)

  return filtered_image

image = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)

kernel_size = int(input('Digite o tamanho da janela que será usada para calcular a média:'))
filtered_image = apply_mean_filter(image, kernel_size)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title(f"Imagem Filtrada (Kernel {kernel_size}x{kernel_size})")
plt.axis("off")

plt.tight_layout()
plt.show()