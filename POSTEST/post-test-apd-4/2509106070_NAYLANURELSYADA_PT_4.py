nama = "nayla nur"
nim = "2509106070"
percobaan = 0
maksimal = 3

while True:
    if percobaan<3:
        username = input("Masukkan Nama Anda: ")
        password = (input("Masukkan NIM Anda: "))
    
    if username == nama and password == nim:
        print("Berhasil Login!")
        break
    
    else:
        percobaan += 1
        sisapercobaan = maksimal-percobaan
        if sisapercobaan >0:
            print(f"Login Gagal! Batas percobaan {3 - percobaan}")
        else :
            print("Anda telah mencapai batas percobaan, Silahkan coba lagi lain kali!")
            exit()
pilihan = (input("\n Apakah anda ingin membeli tiket bioskop? "))

#harga tiket
reguler = 50000
VIP = 100000
VVIP = 150000

while True:
    if pilihan == "ya":
        print ("Berikut adalah pilihan tiket bioskop XX0: ")
    print ("1. Reguler")
    print("2. VIP")
    print("3. VVIP")
    opsi=input ("Pilih Opsi Tiket Anda! ")
    
    if opsi == "reguler":
        print (f"Tiket Reguler dengan harga: Rp {int(reguler)} /tiket")
        hargaTiket = 50000
        jumlahTiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
        totalHarga = 0
        for i in range(jumlahTiket):
            totalHarga += hargaTiket
            print ("Total harga yang harus anda bayar: ",totalHarga)
        if totalHarga >300000:
            diskon = totalHarga - (totalHarga*12/100)
            print ("Selamat anda mendapatkan diskon 12%, menjadi", diskon)
        elif totalHarga >200000:
            diskon = (totalHarga*8/100)
            print ("Selamat anda mendapatkan diskon 8%, menjadi", diskon)
        elif totalHarga >150000:
            print ("Selamat anda mendapatkan poster film eksklusif!")
            
        print ("=== Keterangan ===")
        print("Tiket = Reguler ")
        print(f"Jumlah Tiket = {int(jumlahTiket)}")
        print("Total Harga yang harus dibayar:",diskon)
        break
    elif opsi == "VIP":
        print (f"Tiket VIP dengan harga: Rp {int(VIP)} /tiket ")
        hargaTiket = 100000
        jumlahTiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
        totalHarga = 0
        for i in range(jumlahTiket):
            totalHarga += hargaTiket
            print ("Total harga yang harus anda bayar: ",totalHarga)
        if totalHarga >300000:
            diskon = totalHarga - (totalHarga*12/100)
            print ("Selamat anda mendapatkan diskon 12%, menjadi", diskon)
        elif totalHarga >200000:
            diskon = (totalHarga*8/100)
            print ("Selamat anda mendapatkan diskon 8%, menjadi", diskon)
        elif totalHarga >150000:
            print ("Selamat anda mendapatkan poster film eksklusif!")
            
        print ("=== Keterangan ===")
        print("Tiket = VIP ")
        print(f"Jumlah Tiket = {int(jumlahTiket)}")
        print("Total Harga yang harus dibayar:",diskon)
        break
    elif opsi == "VVIP":
        print (f"Tiket VVIP dengan harga: {int(VVIP)} /tiket")
        hargaTiket = 150000
        jumlahTiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
        totalHarga = 0
        for i in range(jumlahTiket):
            totalHarga += hargaTiket
            print ("Total harga yang harus anda bayar: ",totalHarga)
        if totalHarga >300000:
            diskon = totalHarga - (totalHarga*12/100)
            print ("Selamat anda mendapatkan diskon 12%, menjadi", diskon)
        elif totalHarga >200000:
            diskon = (totalHarga*8/100)
            print ("Selamat anda mendapatkan diskon 8%, menjadi", diskon)
        elif totalHarga >150000:
            print ("Selamat anda mendapatkan poster film eksklusif!")
            
        print ("=== Keterangan ===")
        print("Tiket = VVIP ")
        print(f"Jumlah Tiket = {int(jumlahTiket)}")
        print("Total Harga yang harus dibayar:",diskon)
    else:
        print ("Silahkan coba lagi!")
    
else:
    print("Silahkan Coba Lagi!")