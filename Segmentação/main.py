import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_valley_threshold(hist):
    peaks = np.argsort(hist)[-2:] 
    p1, p2 = sorted(peaks) 

  
    valley = np.argmin(hist[p1:p2]) + p1
    return valley

def segment_image(image, threshold):
    _, binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary

image = cv2.imread('imagem2.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image], [0], None, [256], [0, 256]).ravel()

threshold = find_valley_threshold(hist)

binary_image = segment_image(image, threshold)

plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.plot(hist, color='black')
plt.axvline(x=threshold, color='red', linestyle='--', label=f'Limiar: {threshold}')
plt.title("Histograma")
plt.legend()

plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap='gray')
plt.title("Imagem Segmentada")
plt.axis("off")

plt.tight_layout()
plt.show()