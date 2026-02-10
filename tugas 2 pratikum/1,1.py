def rata_rata(nilai):
    if not nilai:
        return "Data kosong"
    
    
    total = sum(nilai)
    jumlah_data = len(nilai)
    hasil = total / jumlah_data # Menghitung rata-rata
    
    return hasil

# mengisi nilai mahasiswa
data_mahasiswa = [80, 75, 90, 60, 85]
hasil_perhitungan = rata_rata(data_mahasiswa)

# menampilkan hasil ke layar
print(f"List Nilai: {data_mahasiswa}")
print(f"Rata-rata: {hasil_perhitungan}")

#jika list kosong
print(f"Uji list kosong: {rata_rata([])}")