import math

def jarak(x1, y1, x2, y2):
    # Menghitung selisih x dan y, lalu dikuadratkan
    dx_kuadrat = (x2 - x1)**2
    dy_kuadrat = (y2 - y1)**2
    
    # Menghitung akar kuadrat dari jumlah kuadrat tadi
    d = math.sqrt(dx_kuadrat + dy_kuadrat)
    
    return d

x1, y1 = 3, 3
x2, y2 = 5, 10

hasil = jarak(x1, y1, x2, y2)
print("Jarak =", hasil)