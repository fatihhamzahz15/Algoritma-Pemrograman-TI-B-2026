def pangkat_rekursif(a, b):
    # jika pangkatnya adalah 0
    if b == 0:
        return 1
    # a dikalikan dengan fungsi itu sendiri tapi b dikurangi 1
    else:
        return a * pangkat_rekursif(a, b - 1)

# Pengujian sesuai data contoh diberikan
a = 2
b = 5
hasil = pangkat_rekursif(a, b)

print(f"Input: a = {a}, b = {b}")
print(f"Output: {hasil}")