import face_recognition
import os
import pickle
import re

KNOWN_FACES_DIR = 'data'
encodings_dict = {}

for filename in os.listdir(KNOWN_FACES_DIR):
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    base_name = re.match(r"(.+?)_\d+\.(jpg|jpeg|png)", filename)
    if base_name:
        name = base_name.group(1)
    else:
        name = os.path.splitext(filename)[0]

    image = face_recognition.load_image_file(os.path.join(KNOWN_FACES_DIR, filename))
    encodings = face_recognition.face_encodings(image)

    if encodings:
        if name not in encodings_dict:
            encodings_dict[name] = []
        encodings_dict[name].append(encodings[0])
        print(f"[✓] {filename} işlendi ve {name} olarak eklendi.")
    else:
        print(f"[X] Yüz bulunamadı: {filename}")

with open('encodings.pickle', 'wb') as f:
    pickle.dump(encodings_dict, f)
