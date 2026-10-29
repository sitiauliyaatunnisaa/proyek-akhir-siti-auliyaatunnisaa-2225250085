# Skenario Pengujian (Test Case) - Program Analisis Nilai

Dokumen ini berisi daftar skenario pengujian unit dan integrasi untuk memastikan bahwa setiap modul dalam proyek program analisis nilai matematika berjalan dengan benar dan bebas dari kesalahan (*error*).

## Tabel Skenario Pengujian

| ID Test Case | Modul yang Diuji | Jenis Uji | Input / Kondisi | Expected Result (Hasil Harapan) | Status Aktual |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC01** | `analisis.py` | Normal | Daftar nilai: `[80, 90, 70]` | Menghasilkan rata-rata = `80.0`, Max = `90`, Min = `70` | Lolos / Berhasil |
| **TC02** | `analisis.py` | Batas | Nilai siswa tepat di angka KKM (`75`) | Menentukan status ketuntasan menjadi `"Tuntas"` | Lolos / Berhasil |
| **TC03** | `analisis.py` | Batas | Nilai siswa di bawah KKM (`74`) | Menentukan status ketuntasan menjadi `"Remedial"` | Lolos / Berhasil |
| **TC04** | `data_io.py` | Normal | Berkas `data/nilai_contoh.txt` tersedia | Program berhasil membaca seluruh baris data siswa dan mengubahnya menjadi *dictionary* | Lolos / Berhasil |
| **TC05** | `data_io.py` | Invalid | Berkas data kosong atau tidak ditemukan | Program mencetak pesan peringatan tanpa mengalami *crash* (*error*) | Lolos / Berhasil |
| **TC06** | `main.py` | Integrasi | Menjalankan program utama via terminal (`python3 src/main.py`) | Berkas laporan otomatis terbentuk di `output/laporan_analisis.txt` dengan format yang rapi | Lolos / Berhasil |

## Catatan Pengujian
Seluruh skenario pengujian di atas telah diuji secara mandiri melalui lingkungan eksekusi Python di VS Code dan terbukti menghasilkan keluaran yang sesuai dengan rancangan spesifikasi program.