def bilangan_prima(n):
    daftar_prima = []
    
    for angka in range(1, n + 1):
        if angka > 1:
            # Asumsikan angka adalah prima
            is_prima = True
            for i in range(2, int(angka**0.5) + 1):
                if (angka % i) == 0:
                    is_prima = False
                    break
            
            if is_prima:
                daftar_prima.append(angka)
                
    return daftar_prima

# masukkan nilai n = 50
n_input = 50
hasil_prima = bilangan_prima(n_input)

# menampilkan hasil
print(f"Bilangan prima dari 1 sampai {n_input}:")
print(hasil_prima)