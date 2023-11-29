import cv2
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

img=cv2.imread('img1.jpeg',0)
min_intensity=np.min(img)
max_intensity=np.max(img)
stretched_img=(((img-min_intensity)/(max_intensity-min_intensity))*255).astype(np.uint8)
equalized_img=cv2.equalizeHist(img)

hist_original=cv2.calcHist([img],[0],None,[256],[0,255])
hist_stretched=cv2.calcHist([stretched_img],[0],None,[256],[0,255])
hist_equalized=cv2.calcHist([equalized_img],[0],None,[256],[0,255])

plt.figure(figsize=(12,8))
 
plt.subplot(231)
plt.title('original image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(232)
plt.title('stretched image')
plt.imshow(stretched_img,cmap='gray')
plt.axis('off')

plt.subplot(233)
plt.title('equalized image')
plt.imshow(equalized_img,cmap='gray')
plt.axis('off')

plt.subplot(234)
plt.title('histogram original')
plt.plot(hist_original)
plt.xlim([0,256])

plt.subplot(235)
plt.title('histogram stretched')
plt.plot(hist_stretched)
plt.xlim([0,256])


plt.subplot(236)
plt.title('histogram equalised')
plt.plot(hist_equalized)
plt.xlim([0,256])
plt.show()







