import cv2
from utils import image_show
import numpy as np

image_path = "./cat.jpg"
image = cv2.imread(image_path)

#image 10x10 픽셀 크기로 변환
image_color_10x10 = cv2.resize(image,(10,10))
image_color_10x10.flatten()
#image_show(image_color_10x10)

#image 250x250 픽셀 크기로 변환
image_color_250x250 = cv2.resize(image, (250,250))
image_color_250x250.flatten()
#image_show(image_color_250x250)

x = np.array([[51,40],[14,19],[10,7]])
x = x.flatten()
print(x)