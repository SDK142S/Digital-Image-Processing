import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("images/flower.jpg")

# Resize the image
resized_image = cv2.resize(image, (200, 200))

# Rotate the image
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Flip horizontally and vertically
flipped_horizontal = cv2.flip(image, 1)
flipped_vertical = cv2.flip(image, 0)

# Convert to grayscale
gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (85, 85), 0)

# Plot the images
plt.figure(figsize=(12, 8))

plt.subplot(241)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(242)
plt.title("Resized")
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(243)
plt.title("Rotated")
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(244)
plt.title("Horizontal Flip")
plt.imshow(cv2.cvtColor(flipped_horizontal, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(245)
plt.title("Vertical Flip")
plt.imshow(cv2.cvtColor(flipped_vertical, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(246)
plt.title("Grayscale")
plt.imshow(gray_scale, cmap="gray")
plt.axis("off")

plt.subplot(247)
plt.title("Blurred")
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.show()
