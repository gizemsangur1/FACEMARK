# 📸 FaceMark – AI-Powered Smart Attendance System

FaceMark is a real-time face recognition-based attendance system built with Python and AI.  
No cards. No QR codes. Just your face.

---

## 🚀 Features

- 🧠 Face recognition with [`face_recognition`](https://github.com/ageitgey/face_recognition)
- 🎥 Real-time camera support via OpenCV
- 📝 Automatic attendance logging in `attendance.csv`
- 📅 Ensures only one entry per person per day
- ⚡ Fast, lightweight, and works offline

---

## 🖥️ Demo

![screenshot](/facemark.png)  
*Real-time recognition and automatic attendance marking*

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **face_recognition**
- **Pandas**

---

## 🧪 How It Works

1. Place images of registered users in the `dataset/` folder  
2. Run `encode_faces.py` to create face encodings  
3. Start the app with `main.py` – it opens your webcam  
4. When a known face is detected, attendance is saved in `attendance.csv`  
5. Each user is marked only **once per day**

---

## ▶️ Quick Start

```
# Install dependencies
pip install face_recognition opencv-python pandas

# Step 1: Encode registered faces
python encode_faces.py

# Step 2: Run the main attendance app
python main.py

````

## 📊 View Attendance
````
python show_attendance.py
````
