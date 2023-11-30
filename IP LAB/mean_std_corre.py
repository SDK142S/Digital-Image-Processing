import cv2
import numpy as np
img1=cv2.imread("img1.jpeg",0)
img2=cv2.imread("img2.jpeg",0)

mean_img1=np.mean(img1)
sd_img1=np.std(img1)

mean_img2=np.mean(img2)
sd_img2=np.std(img2)

corr=np.corrcoef(img1.flatten(),img2.flatten())[0,1]

print("mean of image1:",mean_img1)
print("mean of image2:",mean_img2)
print("SD of image1:",sd_img1)
print("SD of image2:",sd_img2)
print("correlation coefficient:",corr)
