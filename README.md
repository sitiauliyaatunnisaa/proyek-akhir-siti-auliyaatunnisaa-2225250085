# Program Otomatisasi Analisis Nilai Ujian Siswa

Proyek tugas mandiri ini disusun untuk memenuhi tugas mata kuliah **Algoritma dan Pemrograman** (Program Studi S1 Pendidikan Matematika, FKIP Universitas Sultan Ageng Tirtayasa).

## Deskripsi Proyek
Program ini dirancang menggunakan bahasa Python dengan pendekatan struktur **pemrograman modular**. Program berfungsi untuk membaca data mentah daftar nilai siswa dari berkas eksternal, menghitung statistik kelas secara otomatis (rata-rata, nilai tertinggi, dan terendah), menentukan status ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), serta menyimpan laporan hasil analisis ke dalam berkas teks.

## Struktur Direktori Proyek
```text
proyek-akhir-siti-auliyaatunnisaa-2225250085/
│
├── data/
│   └── nilai_contoh.txt      # Berkas input data mentah siswa
│
├── src/
│   ├── main.py             # Titik masuk utama (entry point) program
│   ├── analisis.py         # Modul logika statistik dan status KKM
│   ├── data_io.py          # Modul manajemen baca file dan simpan laporan
│   └── utilitas.py         # Modul fungsi pendukung dan validasi
│
├── output/
│   └── laporan_analisis.txt  # Berkas hasil keluaran analisis otomatis
│
├── tests/
│   └── test_case.md        # Dokumen skenario pengujian (test case)
│
├── proposal.md             # Dokumen proposal perancangan proyek
├── .gitignore              # Pengaturan berkas yang diabaikan oleh Git
└── README.md               # Dokumentasi utama proyek

```

## Cara Menjalankan Program

Pastikan Anda sudah menginstal Python di komputer Anda. Buka terminal pada aplikasi **VS Code**, lalu jalankan perintah berikut di direktori utama proyek:

```bash
python src/main.py
```
## Penulis

* **Nama:** Siti Auliyaatunnisaa
* **NIM:** 2225250085
* **Program Studi:** S1 Pendidikan Matematika

```
