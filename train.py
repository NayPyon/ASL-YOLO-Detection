from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8n.pt') 
    
    # 2. Memulai proses training
    print("Memulai proses training...")
    results = model.train(
        data='./dataset/data.yaml', # Path ke file data.yaml
        epochs=50,                  # Jumlah putaran belajar (50 cukup untuk awal)
        imgsz=640,                  # Resolusi gambar (standar YOLO)
        batch=16,                   # Jumlah gambar yang diproses bersamaan. 
                                    # (Jika VRAM GPU kamu kecil dan muncul error "Out of Memory", ubah ke 8 atau 4)
        device=0,                   # 0 berarti menggunakan GPU NVIDIA pertamamu
        workers=2,                  # Mencegah CPU bottleneck di Windows
        name='asl_model_v1'         # Nama folder hasil training nanti
    )
    print("Training Selesai!")