# **FaceDistanceMeasure** 📏📸  
_A project to estimate the distance of a face from a camera using computer vision._

---

## 🌟 **Features**
- 🎥 **Real-time face detection.**
- 📏 **Accurate distance measurement** based on the size of the detected face.
- 📂 **Easy-to-use and extend** for other object distance measurements.
- 🧠 **Utilizes OpenCV and Haar Cascade** for efficient face detection.

---

## 🔧 **Requirements**
Make sure you have the following installed:
- **Python 3.7+**
- **OpenCV 4.x**
- **A working webcam or camera device**

---

## 🚀 **How It Works**
1. **Captures video frames from your webcam.**
2. **Detects faces using the Haar Cascade model.**
3. **Calculates the distance of the face from the camera** using the formula:
   \[
   \text{Distance} = \frac{\text{Real Width of Object} \times \text{Focal Length}}{\text{Width of Object in Frame}}
   \]

---

## 📂 **Project Structure**
```plaintext
📁 Distance_measurement_using_single_camera
├── distance.py                # Main script
├── camera.py                  # Camera testing script
├── Ref_image.png              # Reference image for focal length calculation
├── haarcascade_frontalface_default.xml  # Haar Cascade model for face detection
└── README.md                  # Project documentation


# **FaceDistanceMeasure** 📏📸  
_A project to estimate the distance of a face from a camera using computer vision._

---

## 🛠️ **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/FaceDistanceMeasure.git
   cd FaceDistanceMeasure

## 🤔 **Use Cases**

- 📚 **Educational Purposes**: Learn the basics of computer vision and distance estimation.
- 🛠️ **DIY Projects**: Use it for robotics, surveillance, or smart home systems.
- 🚗 **Automotive Applications**: Estimate distances for autonomous driving or parking systems.
- 🛡️ **Security Systems**: Monitor and measure proximity for restricted areas.

## 📸 **Demo**

Below is a demonstration of the project in action:

![image](https://github.com/user-attachments/assets/898ea9a6-bdc1-4586-a953-8c5c99062477)


In this example, the project detects a face and calculates the distance as **70.76 CM**.


## 📝 **Acknowledgments**

- Created by **Haider Manzoor** ✨.
- Inspired by the awesome community of AI and computer vision enthusiasts.
--

## 🏗️ **Future Improvements**

- 🔍 **Support for multiple objects.**
- ⚡ **Improved performance with deep learning models.**
- 📊 **Detailed analytics and visualizations.**

---

## 💌 **Contributing**

We welcome contributions! Create a pull request or open an issue to get involved.

---

## 📜 **License**

This project is licensed under the [MIT License](LICENSE).


🛡️ Disclaimer
This project is for educational purposes only. Ensure ethical and legal use in your applications.

### **Features of the Beautified Markdown:**
1. **Headings**: Each section has a proper heading using `##`.
2. **Bullet Points**: Use cases, acknowledgments, and improvements are organized as bullet points.
3. **Code Blocks**: Commands (e.g., `git clone`, `pip install`) are in fenced code blocks (` ``` `).
4. **Dividers**: Sections are separated by horizontal rules (`---`) for better readability.
5. **Emojis**: Added relevant emojis for a visually appealing format.

---

