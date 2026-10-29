"""
Modul: data_io.py
Deskripsi: Membaca file data teks dan menyimpan laporan hasil analisis.
"""
import os

def baca_data_nilai(filepath):
    """Membaca file teks berisi daftar nilai siswa dan mengembalikan list dictionary."""
    data_siswa = []
    if not os.path.exists(filepath):
        print(f"[Peringatan] File {filepath} tidak ditemukan.")
        return data_siswa

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Abaikan baris kosong atau komentar (diawali #)
            if line and not line.startswith("#"):
                parts = line.split(",")
                if len(parts) == 2:
                    nama = parts[0].strip()
                    try:
                        nilai = float(parts[1].strip())
                        data_siswa.append({"nama": nama, "nilai": nilai})
                    except ValueError:
                        continue
    return data_siswa

def simpan_laporan(filepath, konten):
    """Menyimpan ringkasan laporan analisis ke dalam direktori tujuan."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(konten)
    print(f"[Info] Laporan berhasil disimpan ke: {filepath}")