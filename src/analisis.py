"""
Modul: analisis.py
Deskripsi: Berisi fungsi untuk perhitungan statistik dan status nilai.
"""

def hitung_statistik(daftar_nilai):
    """Menghitung rata-rata, nilai tertinggi, dan nilai terendah dari list nilai."""
    if not daftar_nilai:
        return 0.0, 0, 0
    
    total = sum(daftar_nilai)
    rata_rata = total / len(daftar_nilai)
    nilai_max = max(daftar_nilai)
    nilai_min = min(daftar_nilai)
    
    return round(rata_rata, 2), nilai_max, nilai_min

def tentukan_status(nilai, kkm=75):
    """Menentukan apakah siswa tuntas atau perlu remedial berdasarkan KKM."""
    if nilai >= kkm:
        return "Tuntas"
    else:
        return "Remedial"