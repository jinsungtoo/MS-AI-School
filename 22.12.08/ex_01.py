#같은 크기의 이미지 블렝딩 실험

import cv2
import matplotlib.pyplot as plt
import numpy as np

large_img = cv2.imread("./ex_image.png")
watermark = cv2.imread("./ex_image_logo.png")

print("large_image_size >> ", large_img.shape)
print("watermark image size >>", watermark.shape)

# cv2.imshow("image large", large_img)
# cv2.imshow("watermark", watermark)
# cv2.waitKey(0)

img1 = cv2.resize(large_img, (800,600))
img2 = cv2.resize(watermark, (800,600))

print("img1 resize >>", img1.shape)
print("img2 resize >>", img2.shape)

#혼합 진행
blended = cv2.addWeighted(img1, 1, img2, 1, 0)
cv2.imshow("image show", blended)
cv2.waitKey(0)