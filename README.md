# Camera-Calibration
Camera calibration using opencv


# 📸 Homework #3 - Camera Calibration

## 🎯 목표

- 내 카메라(노트북/스마트폰 등)를 이용하여 카메라 캘리브레이션 수행
- 렌즈 왜곡 계수를 추정하고, 이를 바탕으로 이미지 왜곡 보정 수행

---

## 📐 Camera Calibration

### ▶ 체스보드 정보
- 사용한 패턴: **9x6 체스보드 (내부 코너 기준)**
- 출력 방법: A4 용지에 출력 후 평평한 바닥에 부착

### ▶ 데이터 수집
- 다양한 시점(정면, 측면, 경사 등)에서 **체스보드를 촬영한 영상**
- 촬영 파일: `data/chessboard.avi`

### ▶ 사용 코드
- `camera_calibration.py`

> ☝️ 실제 값은 calibration_data.npz로부터 불러오거나 수기로 기입

---

## 🛠️ Lens Distortion Correction

### ▶ 사용 코드
- `distortion_correction.py`

### ▶ 설명
- 카메라 캘리브레이션 결과를 이용해 영상에서의 렌즈 왜곡을 제거하였습니다.
- `cv2.undistort()` 및 `cv2.getOptimalNewCameraMatrix()` 사용

### ▶ 데모
- `data/chessboard.avi` 원본 영상과 왜곡 보정 후 결과를 비교 표시
- OpenCV 창으로 두 영상을 동시에 출력: `"Original"` vs `"Undistorted"`

---

## 🧪 실행 방법

### 1. 카메라 캘리브레이션
```bash
python camera_calibration.py
