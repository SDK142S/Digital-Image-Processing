import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread("images/forest.jpg", 0)

# Perform intensity stretching
min_intensity = np.min(img)
max_intensity = np.max(img)
stretched_image = ((img - min_intensity) / (max_intensity - min_intensity) * 255).astype(np.uint8)

# Calculate histograms
hist_original = cv2.calcHist([img], [0], None, [255], [0, 255])
hist_stretched = cv2.calcHist([stretched_image], [0], None, [255], [0, 255])

# Perform histogram equalization
equalized_image = cv2.equalizeHist(img)
hist_equalized = cv2.calcHist([equalized_image], [0], None, [255], [0, 255])

# Plot the images and histograms
plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.title("Original")
plt.imshow(img, cmap="gray")
plt.axis("off")

plt.subplot(232)
plt.title("Stretched")
plt.imshow(stretched_image, cmap="gray")
plt.axis("off")

plt.subplot(233)
plt.title("Equalized")
plt.imshow(equalized_image, cmap="gray")
plt.axis("off")

plt.subplot(234)
plt.title("Histogram Original")
plt.plot(hist_original)
plt.xlim([0, 255])

plt.subplot(235)
plt.title("Histogram Stretched")
plt.plot(hist_stretched)
plt.xlim([0, 255])

plt.subplot(236)
plt.title("Histogram Equalized")
plt.plot(hist_equalized)
plt.xlim([0, 255])

plt.tight_layout()
plt.show()
