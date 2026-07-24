import cv2
from ultralytics import YOLO

# 1. Load model 
model_path = r"runs\detect\asl_model_v1-2\weights\best.pt"
model = YOLO(model_path)

# 2. Buka kamera
cap = cv2.VideoCapture(0)

# 3. ATUR RESOLUSI
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Gagal membaca kamera.")
        break

    # 4. PERBAIKI MIRRORING: Balikkan gambar secara horizontal
    frame = cv2.flip(frame, 1)

    # 5. Jalankan prediksi
    results = model.predict(frame, conf=0.7, show=False)

    annotated_frame = results[0].plot()

    cv2.imshow("Deteksi ASL", annotated_frame)

    # 6. Tekan tombol 'q' di keyboard untuk keluar jendela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()