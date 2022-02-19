import cv2
import numpy as np

img = cv2.imread("C:/Users/MSDL-DESK-02/Desktop/data1/img.png")
size = img.shape

#2차원 영상좌표
points_2D = np.array([
                        (966, 543),  #좌 하단 
                        (1155, 554),  #우 하단
                        (975, 363),  #좌 상단
                        (1159, 369),  #우 상단
                      ], dtype="double")
                      
#3차원 월드좌표
points_3D = np.array([
                      (0.0, 0.0, 0.0),       #좌 하단
                      (10, 0.0, 0.0),        #우 하단
                      (0.0, 10, 0.0),        #좌 상단
                      (10, 10, 0.0)          #우 상단
                     ], dtype="double")


# camera 내부 파라미터 
cameraMatrix = np.array([[1065.352, 0, 960.127], [0, 1064.480, 569.483], [0, 0, 1]])

#distcoeffs는 카메라의 왜곡을 무시하기 때문에 null값 전달
dist_coeffs = np.zeros((4,1))

#solvePnp 함수적용
retval, rvec, tvec = cv2.solvePnP(points_3D, points_2D, cameraMatrix, dist_coeffs, rvec=None, tvec=None, useExtrinsicGuess=None, flags=None)
R = cv2.Rodrigues(rvec)
T = tvec

print(R)
# print("\n")
print(T)