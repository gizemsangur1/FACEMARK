import face_recognition
import cv2
import pickle
import pandas as pd
from datetime import datetime
import os

with open('encodings.pickle', 'rb') as f:
    known_faces = pickle.load(f)

video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Kamera açılamadı.")
    exit()

print("Kamera çalışıyor. Çıkmak için 'q' tuşuna bas.")

marked_today = set()
today_str = datetime.now().strftime("%Y-%m-%d")

if os.path.exists("attendance.csv"):
    df_prev = pd.read_csv("attendance.csv", names=["Name", "Date", "Time"])
    marked_today = set(df_prev[df_prev["Date"] == today_str]["Name"])

while True:
    ret, frame = video.read()
    if not ret:
        print("Görüntü alınamadı.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)

    for face_location in face_locations:
        try:
            face_encoding = face_recognition.face_encodings(rgb_frame, [face_location])[0]
        except Exception as e:
            print(f"[HATA] Encoding alınamadı: {e}")
            continue

        name_found = "Unknown"

        for name, enc_list in known_faces.items():
            matches = face_recognition.compare_faces(enc_list, face_encoding, tolerance=0.45)
            if True in matches:
                name_found = name
                break

        top, right, bottom, left = face_location
        color = (0, 255, 0) if name_found != "Unknown" else (0, 0, 255)

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        cv2.putText(frame, name_found, (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        if name_found != "Unknown" and name_found not in marked_today:
            now = datetime.now()
            df = pd.DataFrame([[name_found, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")]],
                              columns=["Name", "Date", "Time"])
            df.to_csv("attendance.csv", mode='a', header=not os.path.exists("attendance.csv"), index=False)
            print(f"[✓] Yoklama alındı: {name_found}")
            marked_today.add(name_found)

    cv2.imshow("Face Recognition Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
