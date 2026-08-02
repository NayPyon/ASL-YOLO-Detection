# 🤟 American Sign Language (ASL) Detection using YOLOv8

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logo=YOLO&logoColor=black)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

Selamat datang di *repository* proyek Deteksi American Sign Language (ASL)! Proyek ini menggunakan model *Computer Vision* (YOLOv8) untuk mengenali dan menerjemahkan bahasa isyarat tangan secara *real-time* langsung melalui *webcam*.

## ✨ Fitur Utama
* **Deteksi Real-Time:** Mengenali isyarat tangan ASL dengan cepat tanpa *delay*.
* **Anti-Mirroring:** Tampilan kamera telah dikalibrasi agar tidak terbalik, memastikan deteksi tangan kanan/kiri tetap presisi.
* **Filter False-Positive:** Dilengkapi dengan *confidence threshold* khusus untuk mengabaikan deteksi palsu seperti wajah atau latar belakang.
* **Ringan & Cepat:** Menggunakan arsitektur model yang efisien sehingga dapat berjalan lancar di komputer standar.

## 📂 Struktur Direktori
* `tes_webcam.py` : *Script* utama untuk menjalankan deteksi *real-time*.
* `train.py` : *Script* untuk melatih (training) model pada dataset ASL.
* `requirements.txt` : Daftar pustaka (*library*) yang dibutuhkan.
* `runs/detect/` : Folder berisi hasil pelatihan dan bobot model terbaik (`best.pt`).

## ⚙️ Cara Instalasi (Untuk Pengguna Lain)

Jika Kamu ingin mencoba menjalankan model ini di komputer Kamu, ikuti langkah berikut:

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/NayPyon/ASL-YOLO-Detection.git
   ```
   
 2. **Install semua requirement:**
   ```bash
  pip install -r requirements.txt
  ```
## 🎥 Cara Penggunaan

Pastikan webcam Kamu terhubung, lalu jalankan perintah berikut di terminal:

```bash
python tes_webcam.py
```

Catatan: Tekan tombol 'q' pada keyboard saat berada di jendela kamera untuk keluar dari program.

## 🤝 Penggunaan Model `best.pt`
Bagi developer yang hanya ingin menggunakan bobot model (weights) untuk aplikasinya sendiri, silakan 
unduh file `best.pt` yang ada di dalam folder `runs/detect/.../weights/`, lalu muat menggunakan library 
Ultralytics YOLO.

By: NayPyon
