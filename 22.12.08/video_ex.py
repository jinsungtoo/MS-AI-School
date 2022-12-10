import cv2

##### 동영상 속성 확인 #####
cap = cv2.VideoCapture("./video01.mp4") #0으로 설정 시 웹캠 카메라를 보여줌
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

print("width: ", width, "height: ", height)
print("fps:", fps)
print("frame_count: ", frame_count)

##### 동영상 파일 읽기 #####
if cap.isOpened(): # 캡쳐 객체 초기화 확인
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("video file shoe", frame)
            cv2.waitKey(25) # 25프레임 기준
        else:
            break
else:
    print("비디오 파일 읽기 실패")

cap.release()
cv2.destroyAllWindows()