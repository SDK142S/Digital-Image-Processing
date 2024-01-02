import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image in grayscale
img = cv2.imread("images/forest.jpg", 0)

# Create a list to store bit planes
bit_planes = []

# Extract bit planes
for i in range(8):
    plane = np.zeros_like(img, dtype=np.uint8)
    plane[img & (1 << i) != 0] = 255
    bit_planes.append(plane)

# Plot the bit planes
plt.figure(figsize=(12, 6))
for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(bit_planes[i], cmap="gray")
    plt.title(f"BIT_PLANE: {i + 1}")

plt.tight_layout()
plt.show()
