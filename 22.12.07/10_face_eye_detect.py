import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#이미지 불러오기
face_img = cv2.imread('face.png')

face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(face_gray, 1.1, 4)

##얼굴 박스 설정
for (x,y,w,h) in faces:
    cv2.rectangle(face_img, (x,y), (x+w,y+h), (0,255,0), 3)

    roi_img = face_img[y:y+h, x:x+w]
    roi_gray = face_gray[y:y+h, x:x+w]
    # cv2.imshow('roi',roi_img)
    # cv2.waitKey(0)

    # cv2.imshow('face box',face_img)
    # cv2.waitKey(0)

##눈 박스 설정
eyes = eye_cascade.detectMultiScale(roi_gray,1.1,4)
index = 0

for (x,y,w,h) in eyes:
    if index ==0:
        eye_1 = (x,y,w,h)
    elif index == 1:
        eye_2 = (x,y,w,h)

    cv2.rectangle(roi_img, (x,y), (x+w,y+h), (0,255,0), 3)
    index = index+1

    cv2.imshow('face box', face_img)
    cv2.waitKey(0)

    # if eye_1[0] < eye_2[0]:
    #     left_eye = eye_1
    #     right_eye = eye_2
    # else:
    #     left_eye = eye_2
    #     right_eye = eye_1


# left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
