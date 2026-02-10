def jumlah_digit(n):
    # jika n adalah satu digit
    if n < 10:
        return n
    else:
        # Digit terakhir + jumlah_digit dari sisa angkanya
        return (n % 10) + jumlah_digit(n // 10)

# masukkan angka
input_angka = 1234
hasil = jumlah_digit(input_angka)

print(f"Input: {input_angka}")#menampilkan input
print(f"Output: {hasil}")# menampilkan output