import cv2
import numpy as np

mtx = np.array([[fx, 0, cx],
                [0, fy, cy],
                [0, 0, 1]])  # ← fx, fy, cx, cy 직접 대입
dist = np.array([k1, k2, p1, p2, k3])  # ← distortion 계수 직접 대입

cap = cv2.VideoCapture("data/chessboard.avi")
ret, frame = cap.read()
h, w = frame.shape[:2]

newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

while ret:
    dst = cv2.undistort(frame, mtx, dist, None, newcameramtx)

    cv2.imshow("Original", frame)
    cv2.imshow("Undistorted", dst)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()
