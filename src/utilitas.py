"""
Modul: utilitas.py
Deskripsi: Berisi fungsi bantu untuk validasi dan estetika terminal.
"""

def validasi_rentang_nilai(nilai):
    """Memastikan nilai berada dalam rentang 0 sampai 100."""
    try:
        val = float(nilai)
        if 0 <= val <= 100:
            return True
        return False
    except ValueError:
        return False

def cetak_garis(panjang=40):
    """Mencetak garis pemisah untuk estetika antarmuka konsol."""
    print("=" * panjang)