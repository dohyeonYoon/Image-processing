import cv2   # OpenCV import
import numpy as np  # 행렬(img)를 만들기 위한 np import

# 마우스 이벤트 콜백함수 정의
def mouse_callback(event, x, y, flags, param): 
    print("마우스 이벤트 발생, x:", x ," y:", y) # 이벤트 발생한 마우스 위치 출력

img = cv2.imread("C:/Users/MSDL-DESK-02/Desktop/data1/img.png")

cv2.namedWindow('image')  #마우스 이벤트 영역 윈도우 생성
cv2.setMouseCallback('image', mouse_callback)

while(True):

    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:    # ESC 키 눌러졌을 경우 종료
        print("ESC 키 눌러짐")
        break
cv2.destroyAllWindows()