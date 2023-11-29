import cv2
gray_image=cv2.imread('img1.jpeg',cv2.IMREAD_GRAYSCALE)
negative_gray_image=255-gray_image
cv2.imshow('negative grayscale image',gray_image)
cv2.waitKey(0)

cv2.imshow('negative_gray_image',negative_gray_image)
cv2.waitKey(0)