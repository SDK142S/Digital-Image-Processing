import cv2
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
image=cv2.imread('img1.jpeg')
plt.figure(figsize=(12,8))
plt.subplot(241)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(242)
resized_image=cv2.resize(image,(200,200))
plt.imshow(cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB))
plt.axis('off')


plt.subplot(243)
rotated_image=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
plt.imshow(cv2.cvtColor(rotated_image,cv2.COLOR_BGR2RGB))
plt.axis('off')


plt.subplot(244)
flipped_horizontal=cv2.flip(image,1)
plt.imshow(cv2.cvtColor(flipped_horizontal,cv2.COLOR_BGR2RGB))
plt.axis('off')


plt.subplot(245)
fipped_vertical=cv2.flip(image,0)
plt.imshow(cv2.cvtColor(fipped_vertical,cv2.COLOR_BGR2RGB))
plt.axis('off')


plt.subplot(246)
grayscale_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(grayscale_image,cmap='gray')
plt.axis('off')

plt.subplot(247)
blurred_image=cv2.GaussianBlur(image,(15,15),0)
plt.imshow(cv2.cvtColor(blurred_image,cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()