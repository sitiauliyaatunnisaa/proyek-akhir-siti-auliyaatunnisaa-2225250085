# PROPOSAL PROYEK AKHIR / TUGAS MANDIRI

## Mata Kuliah: Algoritma dan Pemrograman (S1 Pendidikan Matematika FKIP Untirta)

### 1. Judul Proyek

**Program Otomatisasi Analisis Nilai Ujian Siswa Berbasis Modular Python**

### 2. Latar Belakang Masalah

Dalam kegiatan pembelajaran matematika di sekolah, seorang guru sering kali dihadapkan pada kebutuhan untuk mengolah data nilai ujian siswa secara cepat dan akurat. Pengolahan nilai secara manual—seperti mencari nilai rata-rata, menentukan nilai tertinggi dan terendah, serta mengelompokkan status kelulusan berdasarkan Kriteria Ketuntasan Minimal (KKM)—membutuhkan waktu yang tidak sedikit dan rentan terhadap kesalahan hitung. Oleh karena itu, diperlukan sebuah program aplikasi berbasis teks (*command-line interface*) menggunakan bahasa Python yang mampu membaca data nilai dari berkas eksternal, melakukan perhitungan statistik secara otomatis, dan menyajikannya dalam bentuk laporan rekapitulasi yang terstruktur.

### 3. Pengguna Utama dan Tujuan Proyek

* **Pengguna Utama:** Guru matematika, tenaga kependidikan, atau mahasiswa.
* **Tujuan Program:** Membantu pengguna memproses data nilai ujian secara otomatis, menghitung statistik kelas (rata-rata, maksimum, minimum), menentukan status ketuntasan siswa berdasarkan KKM, serta menyimpan laporan hasil analisis ke dalam berkas teks eksternal.

### 4. Ruang Lingkup Proyek

* **Fitur Utama (Core Features):**
1. Membaca data mentah dari berkas teks eksternal (`data/nilai_contoh.txt`).
2. Melakukan validasi baris data untuk mencegah kesalahan (*error* pembacaan format).
3. Menghitung nilai rata-rata kelas, nilai tertinggi, dan nilai terendah secara otomatis.
4. Menentukan status siswa ("Tuntas" atau "Remedial") berdasarkan standar KKM yang ditentukan (misalnya KKM = 75).
5. Menyimpan hasil rekapitulasi laporan secara otomatis ke dalam direktori keluaran (`output/laporan_analisis.txt`).


* **Batasan Proyek:** Program berjalan secara mandiri di terminal/konsol (*command-line*) dengan menggunakan struktur pemrograman modular berbasis Python.

### 5. Analisis Kebutuhan (*Requirements*)

* **Kebutuhan Fungsional:**
* `F01`: Program dapat membaca berkas teks yang berisi daftar nama dan nilai siswa.
* `F02`: Program memproses daftar nilai menjadi angka numerik untuk analisis statistik.
* `F03`: Program mengelompokkan status siswa berdasarkan perbandingan nilai terhadap KKM.
* `F04`: Program mencetak ringkasan laporan ke terminal dan menyimpannya ke dalam file teks.


* **Kebutuhan Non-Fungsional:**
* Kode sumber dirancang secara modular dan terpisah ke dalam beberapa berkas (`main.py`, `analisis.py`, `data_io.py`, `utilitas.py`) agar mudah dirawat dan dikembangkan.



### 6. Spesifikasi Input, Proses, dan Output (IPO)

| Input | Proses | Output |
| --- | --- | --- |
| Berkas teks berisi data mentah nama dan nilai (`data/nilai_contoh.txt`). | Membaca berkas $\rightarrow$ Validasi baris $\rightarrow$ Hitung statistik (rata-rata, max, min) $\rightarrow$ Evaluasi status KKM. | Tampilan hasil di terminal konsol dan berkas laporan teks di folder `output/laporan_analisis.txt`. |

### 7. Algoritma dan Pseudocode

```text
MULAI
    Tentukan path berkas data nilai
    Panggil fungsi baca_data_nilai() untuk mengambil data dari file teks
    JIKA data kosong:
        Tampilkan pesan peringatan
        KELUAR
    
    Ekstrak daftar angka nilai siswa
    Hitung rata-rata, nilai maksimum, dan nilai minimum menggunakan fungsi statistik
    
    UNTUK setiap data siswa dalam daftar:
        Tentukan status ketuntasan (Tuntas / Remedial) berdasarkan KKM 75
        Tampilkan hasil ke terminal dan susun format teks laporan
        
    Panggil fungsi simpan_laporan() untuk menulis hasil ke folder output/
    Tampilkan pesan sukses
SELESAI

```

### 8. Struktur Program dan Modularisasi

Proyek ini diorganisasikan ke dalam struktur direktori modular berikut:

```text
proyek-anda/
|-- README.md
|-- proposal.md
|-- .gitignore
|-- data/
|   `-- nilai_contoh.txt
|-- src/
|   |-- main.py          # Pusat kendali dan eksekusi utama
|   |-- analisis.py      # Logika perhitungan statistik dan KKM
|   |-- data_io.py       # Manajemen baca file teks dan simpan laporan
|   `-- utilitas.py      # Fungsi pendukung estetika dan validasi
|-- tests/
|   `-- test_case.md
`-- output/
    `-- .gitkeep

```

### 9. Pemilihan Struktur Data

* **List (Daftar):** Digunakan untuk menampung kumpulan data dictionary siswa serta daftar angka nilai yang akan diiterasi menggunakan perulangan (`for`).
* **Dictionary (Kamus):** Digunakan untuk memetakan atribut data siswa secara berpasangan, yaitu kunci `'nama'` dan `'nilai'`.

### 10. Skenario Pengujian (*Test Case*)

| ID Test Case | Jenis Uji | Kondisi / Input | Hasil yang Diharapkan (*Expected Result*) | Status |
| --- | --- | --- | --- | --- |
| **TC01** | Normal | `[80, 90, 70]` pada modul `analisis.py` | Rata-rata = 80.0, Max = 90, Min = 70 | Lolos |
| **TC02** | Batas | Nilai tepat pada KKM (`75`) | Status bernilai "Tuntas" | Lolos |
| **TC03** | Normal | Berkas `nilai_contoh.txt` tersedia | Program berhasil membaca seluruh baris data siswa | Lolos |
| **TC04** | Normal | Eksekusi `src/main.py` | Berkas `output/laporan_analisis.txt` berhasil terbentuk | Lolos |

