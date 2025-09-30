angka = 10
if angka > 5:
    print ("angka lebih besar dari 5")
else: 
    print ("angka lebih kecil dari 5")


nilai = int(input("Masukan nilai anda: "))

if nilai >= 80:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 60:
    print("C")
else:
    print("Tidak Lulus")



# input nilai
umur = int(input("Masukkan umur Anda: "))
# misalnya, umur = 16
# Percabangan
if umur < 13:
    kategori = "Anak-anak"
elif umur < 18:
    kategori = "Remaja"
elif umur < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"
# Menampilkan umur dan kategori
print("Umur:", umur, "Kategori:", kategori)



# input nilai
umur = int(input("Masukkan umur Anda: "))
# misalnya, umur = 16
# Percabangan
if umur < 13:
    kategori = "Anak-anak"
elif umur < 18:
    kategori = "Remaja"
elif umur < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"
# Menampilkan umur dan kategori
print("Umur:", umur, "Kategori:", kategori)


harga = int(input("Masukan harga: "))

if harga > 10000:
    print ("selamat anda mendapatkan diskon 20%")
elif harga > 50000:
    print ("Selamat anda mendapatkan diskon 10%")
else:
    print ("Anda tidak mendapatkan diskon :(...)")