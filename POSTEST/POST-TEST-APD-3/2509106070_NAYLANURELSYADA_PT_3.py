# user mengisi data
nama = input("Masukan nama anda :")
nim = input("Masukan NIM anda :")

# hitung harga akun premium + biaya admin
Bronze = 1500000 + (1500000*1/100) # harga paket bronze
Silver = 1500000 + (1500000*3/100) # harga paket silver
Gold = 1500000 + (1500000*5/100) # harga paket gold
Platinum = 1500000 + (1500000*7/100) #harga paket silver

if nama == "nayla" and nim == "2509106070" :
    print ("Anda berhasil login!, pilih opsi langganan anda!")
    
    # pilihan opsi biaya langganan aplikasi musik
    print ("Pilih paket Premium anda dan dengarkan musik bebas iklan tanpa batas di ponsel, speaker,dan perangkat lainnya. Bayar dengan berbagai cara, dan anda juga bisa membatalkannya kapan saja.")
    print ("============================================================================================================================")
    print ("Paket Bronze : Pembatalan kapan saja, Lagu-lagu Populer.")
    print ("Paket Silver : 1 Akun Premium, Pembatalan kapan saja, Custom Playlist.")
    print ("Paket Gold : 1 Akun Premium, Pembatalan kapan saja, Custom Playlist, Mode Offline. ")
    print ("Paket Platinum : 1 Akun premium, Akses semua fitur, Custom Playlist, Mode offline, Konten Eksklusif artis.")
    opsi = input("pilih opsi langganan anda! ")
    
    # tampilkan harga
    if opsi == "bronze":
        print (f"Harga Paket Bronze : Rp {int(Bronze)}")
    elif opsi == "silver":
        print (f"Harga Paket Silver : Rp {int(Silver)}")
    elif opsi == "gold":
        print (f"Harga Paket Gold   : Rp {int(Gold)}")
    elif opsi == "platinum":
        print (f"Harga Paket Platinum   : Rp {int(Platinum)}")
    input ("Apakah anda sudah yakin ingin berlangganan opsi tersebut? ")
    print ("Berikut adalah opsi pembayaran yang bisa anda lakukan: ")
    print ("-ShopeePay")
    print ("-Gopay")
    print ("-Transfer Bank")
    
    bayar = input ("Pilih opsi pembayaran anda: ")    
    if bayar == "shopeepay":
        input ("Salin kode pembayaran ini : 123081234567891 = ")
        print ("Selamat anda telah berlangganan musik premium saat ini!, Anda bisa membatalkannya kapanpun.")
    elif bayar == "gopay":
        input ("Salin kode pembayaran ini : 091081351776631 = ")
        print ("Selamat anda telah berlangganan musik premium saat ini!, Anda bisa membatalkannya kapanpun.")
    elif bayar == "transfer bank":
        input ("Salin kode virtual akun anda: 732694867 = ")
        print ("Selamat anda telah berlangganan musik premium saat ini!, Anda bisa membatalkannya kapanpun.")
else:
    print ("Silahkan coba lagi!")
