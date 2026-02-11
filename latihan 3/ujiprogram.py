import myOOP

# A. INHERITANCE (Pewarisan)
print(myOOP.ProdukElektronik("kulkas",15000000,"1 tahun").info_produk())
print(myOOP.ProdukMakanan("yakult",4000,"17 Agustus 2026").info_produk())
print()

#B. POLYMORPHISM
print(myOOP.NotifikasiEmail("ada email baru nichh").kirim())
print(myOOP.NotifikasiSMS("ada SMS baru nichh").kirim())
print()

#C. ENCAPSULATION
m1 = myOOP.Mahasiswa("hamzul",99)
print(m1.get_nilai())

m1.set_nilai(-1)
print(m1.get_nilai())