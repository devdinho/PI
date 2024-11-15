import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_images(images, titles, cmap="gray"):
    plt.figure(figsize=(12, 6))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(img, cmap=cmap)
        plt.title(title)
        plt.axis("off")
    plt.tight_layout()
    plt.show()

binary_image = np.zeros((200, 200), dtype=np.uint8)
cv2.rectangle(binary_image, (50, 50), (150, 150), 255, -1)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(binary_image, kernel, iterations=1)
dilation = cv2.dilate(binary_image, kernel, iterations=1)

grayscale_image = np.zeros((200, 200), dtype=np.uint8)
cv2.circle(grayscale_image, (100, 100), 50, 128, -1)
cv2.circle(grayscale_image, (100, 100), 30, 255, -1)

gradient = cv2.morphologyEx(grayscale_image, cv2.MORPH_GRADIENT, kernel)

show_images(
    [binary_image, erosion, dilation],
    ["Imagem Binária Original", "Erosão", "Dilatação"],
    cmap="gray"
)

show_images(
    [grayscale_image, gradient],
    ["Imagem em Tons de Cinza Original", "Gradiente Morfológico"],
    cmap="gray"
)