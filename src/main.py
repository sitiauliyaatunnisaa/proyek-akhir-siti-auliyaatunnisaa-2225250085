"""
Program Utama: Analisis Nilai Ujian Siswa (Tugas Mandiri)
Mata Kuliah: Algoritma dan Pemrograman
"""
import os

def baca_data_nilai(filepath):
    """Membaca file teks berisi daftar nilai dan mengembalikan list data dictionary."""
    data_siswa = []
    if not os.path.exists(filepath):
        print(f"[Peringatan] File {filepath} tidak ditemukan.")
        return data_siswa

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Abaikan baris kosong atau komentar (*)
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

def hitung_statistik(daftar_nilai):
    """Menghitung rata-rata, nilai tertinggi, dan nilai terendah."""
    if not daftar_nilai:
        return 0.0, 0, 0
    
    total = sum(daftar_nilai)
    rata_rata = total / len(daftar_nilai)
    nilai_max = max(daftar_nilai)
    nilai_min = min(daftar_nilai)
    
    return round(rata_rata, 2), nilai_max, nilai_min

def tentukan_status(nilai, kkm=75):
    """Menentukan status ketuntasan siswa berdasarkan KKM."""
    return "Tuntas" if nilai >= kkm else "Remedial"

def simpan_laporan(filepath, konten):
    """Menyimpan laporan teks ke dalam folder output."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(konten)
    print(f"[Info] Laporan berhasil disimpan ke: {filepath}")

def main():
    print("=" * 50)
    print("  PROGRAM ANALISIS NILAI MATEMATIKA (TUGAS INDIVIDU)")
    print("  Algoritma dan Pemrograman - S1 Pend. Matematika")
    print("=" * 50)

    # 1. Baca data dari file teks
    path_data = "data/nilai_contoh.txt"
    data_siswa = baca_data_nilai(path_data)

    if not data_siswa:
        print("[Info] Data kosong atau file tidak ada.")
        return

    # 2. Proses Analisis Statistik
    daftar_angka = [s["nilai"] for s in data_siswa]
    rata, nilai_max, nilai_min = hitung_statistik(daftar_angka)

    print(f"\nJumlah Siswa       : {len(data_siswa)}")
    print(f"Rata-rata Kelas    : {rata}")
    print(f"Nilai Tertinggi    : {nilai_max}")
    print(f"Nilai Terendah     : {nilai_min}")
    print("-" * 50)

    # 3. Tampilkan Status Per Siswa & Buat Teks Laporan
    print("\nDaftar Status Siswa (KKM = 75):")
    laporan_teks = "LAPORAN HASIL ANALISIS NILAI MATEMATIKA MANDIRI\n" + "="*45 + "\n"
    
    for idx, siswa in enumerate(data_siswa, 1):
        status = tentukan_status(siswa["nilai"], kkm=75)
        baris = f"{idx}. {siswa['nama']} - Nilai: {siswa['nilai']} ({status})"
        print(baris)
        laporan_teks += baris + "\n"

    laporan_teks += f"\nRingkasan Statistik:\n- Rata-rata: {rata}\n- Tertinggi: {nilai_max}\n- Terendah: {nilai_min}\n"

    # 4. Simpan ke folder output
    path_output = "output/laporan_analisis.txt"
    simpan_laporan(path_output, laporan_teks)
    print("\nProgram selesai dieksekusi dengan sukses!")

if __name__ == "__main__":
    main()