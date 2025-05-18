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

## Usage ▶️

1. Update the script with your known reference values:

```python
Know_distance = 30          # Known distance (cm) 📏  
Know_width_face = 14.3      # Known real face width (cm) 👤
```

2. Run the script:

```bash

python your_script_name.py
```

3. Press q to quit. ❌

---

## How It Works ⚙️

- Calculates the focal length using the known reference distance and face width. 🎯  
- Detects faces in the webcam feed. 👁️‍🗨️  
- Measures the face width in pixels and estimates distance with the formula:

\[
\text{Distance} = \frac{\text{Real Face Width} \times \text{Focal Length}}{\text{Face Width in Image}}
\]

---

## Output Example 📸


![Distance Measurement Output](https://github.com/user-attachments/assets/a4c86415-361d-4aed-9b74-7fee27b5ee00)

---

## Notes 📝

- Use the **same camera** for calibration and live detection. 📷  
- Adjust Haar Cascade parameters if needed for better face detection. 🔧  
- Good lighting improves detection accuracy. 💡  

---

## License 📄

Open source, free to use. 🚀

---

## Connect with Me on LinkedIn 🔗

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/muhammad-haider-manzoor)
