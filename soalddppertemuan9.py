print("----------soal nomor 1----------")
# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. 
# Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
# print(celcius_ke_fahrenheit(0))    # Output: 32.0
# print(celcius_ke_fahrenheit(100))  # Output: 212.0

def celcius_ke_fahrenhait(celcius):
    hasil_konversi = (celcius * 9/5) + 32
    return hasil_konversi

celcius = 0
print(celcius_ke_fahrenhait(0))
print(celcius_ke_fahrenhait(100))

print("----------soal nomor 2----------")
# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. 
# Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
# print(is_genap(4))  # Output: True
# print(is_genap(7))  # Output: False

def is_genap(angka):
    hasil = angka % 2 == 0
    return hasil
print(is_genap(4))
print(is_genap(7))

print("----------soal nomor 3----------")
# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# nilai (80) #lulus
# nilai(60) #gagal

def keterangan_lulus_atau_tidak_lulus(nilai):
    if nilai >= 80:
        return"lulus"
    else:
        return"gagal"
print(keterangan_lulus_atau_tidak_lulus(80))
print(keterangan_lulus_atau_tidak_lulus(60))

print("----------soal nomor 4----------")
# Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
# bilangan(20) # 1,3,5,7,9,11,13,15,17,19

def bilangan_ganjil(a):
    ganjil=[i for i in range (1, a) if i % 2 == 1]
    return ganjil

hasil = bilangan_ganjil(20)
print(hasil)