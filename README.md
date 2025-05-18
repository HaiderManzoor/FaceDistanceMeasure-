# Face Distance Measurement Using OpenCV 🎥📏

This project calculates the distance between a face and the camera in real-time using OpenCV’s Haar Cascade face detector and focal length estimation.

---

## Features ✨

- Real-time face detection via webcam 👁️‍🗨️
- Calculates camera focal length using a reference image 🎯
- Estimates distance from camera to detected face in centimeters 📐
- Displays distance on live video feed 🖥️

---

## Requirements 📋

- Python 3.x 🐍
- OpenCV (`opencv-python`) 🧰
- Webcam 📷
- Reference face image (`rf.png`) with known face width and distance 🖼️
- Haar Cascade XML file (`haarcascade_frontalface_default.xml` in `data/` directory) 📂

---

## Installation 🚀

1. Clone or download the repo. 📥

2. Install OpenCV:

```bash
pip install opencv-python
```

3. Download Haar Cascade XML from OpenCV GitHub and put it in the data/ folder. 📂

---
