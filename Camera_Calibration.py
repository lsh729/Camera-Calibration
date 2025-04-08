import cv2
import numpy as np
import glob

# 체스보드 크기 (교차점 기준, 예: 9x6 체스보드)
chessboard_size = (9, 6)

# 월드 좌표계에서 체스보드의 3D 좌표 생성
objp = np.zeros((np.prod(chessboard_size), 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0],
                       0:chessboard_size[1]].T.reshape(-1, 2)

# 3D 포인트, 2D 이미지 포인트 저장용 리스트
objpoints = []  # 3D point in real world
imgpoints = []  # 2D point in image plane

cap = cv2.VideoCapture("data/chessboard.avi")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    found, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    if found:import cv2
import numpy as np

# 체스보드 내부 코너 개수 (예: 9x6 체스보드)
chessboard_size = (9, 6)

# 월드 좌표계에서 체스보드의 3D 좌표 설정 (z=0 평면)
objp = np.zeros((np.prod(chessboard_size), 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0],
                       0:chessboard_size[1]].T.reshape(-1, 2)

# 3D 점과 2D 점을 저장할 리스트
objpoints = []  # 실제 체스보드 코너 (3D)
imgpoints = []  # 이미지상의 체스보드 코너 (2D)

# 체스보드 영상 열기
cap = cv2.VideoCapture("data/chessboard.avi")

# 마지막 gray 이미지의 shape를 저장하기 위한 변수
image_shape = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image_shape = gray.shape[::-1]  # (width, height)

    # 체스보드 코너 찾기
    found, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    if found:
        objpoints.append(objp)

        # 코너 좌표 정밀화
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11),
                                    (-1, -1),
                                    criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
        imgpoints.append(corners2)

        # 체스보드 코너 그리기
        cv2.drawChessboardCorners(frame, chessboard_size, corners2, found)

    # 화면에 프레임 보여주기
    cv2.imshow('Chessboard Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# image_shape이 None이면 실패로 처리
if image_shape is None:
    print("Error: 체스보드를 감지하지 못했습니다.")
    exit()

# 카메라 캘리브레이션 수행
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, image_shape, None, None)

# 재투영 오차 계산
total_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    total_error += error

rmse = total_error / len(objpoints)

# 결과 출력
print("\n=== Camera Calibration 결과 ===")
print("Camera Matrix (K):\n", mtx)
print("Distortion Coefficients:\n", dist.ravel())
print("Reprojection Error (RMSE): {:.4f}".format(rmse))

        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11),
                                    (-1, -1),
                                    criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
        imgpoints.append(corners2)
        cv2.drawChessboardCorners(frame, chessboard_size, corners2, found)

    cv2.imshow('Chessboard Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# 카메라 캘리브레이션
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None)

# RMSE 계산
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(
        objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    mean_error += error

print("\n===== Calibration Results =====")
print("Camera matrix (K):\n", mtx)
print("Distortion coefficients:\n", dist.ravel())
print("Reprojection error (RMSE): {:.4f}".format(mean_error / len(objpoints)))
