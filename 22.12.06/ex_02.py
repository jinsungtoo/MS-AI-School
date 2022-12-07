#가우시안 블러 : 조금 더 부드러운 블러표현
#야간,저녁 이미지 사용 시에 효과를 덜 받음
import cv2
from utils import image_show

image_path = "./cat.jpg"

#이미지 읽기
image = cv2.imread(image_path)

image_g_blury = cv2.GaussianBlur(image, (15,15),0)
image_show(image_g_blury)