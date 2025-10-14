# Program CRUD Toko Obat (Apotek)
# Data Login (username & password)
akun = "Apoteker"
pw = "123"
percobaan = 0 
maksimal = 3

data_obat = [
    ["A001", "Paracetamol", 50, 5000],
    ["B002", "Amoxcilin", 10, 10000],
    ["C003", "Komix", 15, 7000]
]

# LOGIN
while True:
    if percobaan<3:
        print("===== APOTEK SEHAT =====")
        print("======= LOGIN =======")
        username = input("Masukkan username: ")
        password = (input("Masukkan password: "))
    
    if username == akun and password == pw:
        print("Berhasil Login Sebagai {username}")
        break
    
    else:
        percobaan += 1
        sisapercobaan = maksimal-percobaan
        if sisapercobaan >0:
            print(f"Login Gagal! Batas percobaan {3 - percobaan}")
        else :
            print("Anda telah mencapai batas percobaan, Silahkan coba lagi lain kali!")
            exit()
# MENU             
while True:
    print("\n======= MENU APOTEK =======")
    print("1. Tambah Obat")
    print("2. Lihat Daftar Obat")
    print("3. Ubah Stok/harga Obat")
    print("4. Hapus Obat")
    print("5. Logout")
    opsi = input("Pilih opsi (1-5): ").strip()
    
    if opsi == '1':
        print("\n---- TAMBAH DATA OBAT ----")
        while True:
            kode = input("Masukkan kode obat: ").upper().strip()
            if not kode:
                print("Kode tidak boleh kosong.")
                continue
            
            kode_exists = False
            for obat in data_obat:
                if obat[0] == kode:
                    kode_exists = True
                    break
            
            if kode_exists:
                print(f"kode {kode} sudah ada.")
            else:
                break
            
        nama = input ("Masukkan nama obat: ").strip()
        while not nama:
            print ("Nama obat tidak boleh kosong.")
            nama = input("Masukkan nama obat: ").strip()
            
        while True:
            stok_str = input("Masukkan stok:").strip()
            if stok_str.isdigit() and int(stok_str) >= 0:
                stok = int(stok_str)
                break
            else:
                print("Stok harus berupa bilangan bulat. ")
                
        while True:
            harga_str = input("Masukkan harga: ").strip()
            if harga_str.isdigit() and int(harga_str) >=0:
                harga = int(harga_str)
                break
            else:
                print("Harga harus berupa bilangan bulat.")
                
        data_obat.append([kode, nama, stok, harga])
        print(f"\nObat '{nama}' berhasil ditambahkan!")
        
    elif opsi == '2':
        print("\n----- DAFTAR STOK OBAT -----")
        if not data_obat:
            print("Data obat kosong.")
        else:
            print('-' * 40)
            print(f"{'kode':<8} {'Nama Obat':<18} {'Stok':<6} {'Harga':>6}")
            print("-" * 40)
            for obat in data_obat:
                kode, nama, stok, harga = obat
                print(f"{kode:<8} {nama:<18} {stok:<6} {harga:>6}") 
                print("-" * 40)
                
    elif opsi == '3':
        print("\n----- UBAH DATA OBAT -----")
        if not data_obat:
            print("Data obat kosong.")
            continue
        
        print("-" * 40)
        print(f"{'Kode':<8} {'Nama Obat':<18} {'Stok':<6} {'Harga':>6}")
        print("-"* 40)
        for obat in data_obat:
            print(f"{obat[0]:<8} {obat[1]:<18} {obat[2]:<6} {obat[3]:>6}")
            print("-" * 40 )
            
        found_index = -1
        kode_update = input("Masukkan KODE OBAT yang ingin diubah: ").upper().strip()
        
        for i, obat in enumerate(data_obat):
            if obat[0] == kode_update:
                found_index = i
                continue
            
            if found_index == -1:
                print(f" Kode obat '{kode_update}' tidak ditemukan.")
            else:
                obat_lama = data_obat[found_index]
                print(f"Obat yang diubah: {obat_lama[1]} (Stok: {obat_lama[2]}, Harga: {obat_lama[3]})")
                
                while True:
                    stok_baru_str = input(f"Masukkan Stok Baru (Kosongkan untuk tetap {obat_lama[2]}): ").strip()
                    if not stok_baru_str:
                        stok_baru = obat_lama[2]
                        break
                    elif stok_baru_str.isdigit() and int(stok_baru_str) >= 0:
                        stok_baru = int(stok_baru_str)
                        break
                    else:
                        print(" Stok harus berupa angka bilangan bulat.")

                while True:
                    harga_baru_str = input(f"Masukkan Harga Baru (Kosongkan untuk tetap {obat_lama[3]}): ").strip()
                    if not harga_baru_str:
                        harga_baru = obat_lama[3]
                        break
                    elif harga_baru_str.isdigit() and int(harga_baru_str) >= 0:
                        harga_baru = int(harga_baru_str)
                        break
                    else:
                        print("Harga harus berupa angka bilangan bulat.")
                        
                data_obat[found_index][2] = stok_baru
                data_obat[found_index][3] = harga_baru
                print(f"\nData obat '{obat_lama[1]}' berhasil diperbarui!")
                
    elif opsi == '4':
        print("\n----- HAPUS DATA OBAT -----")
        if not data_obat:
            print("Data obat kosong. Tidak ada yang bisa dihapus")
            continue
        
        print("-" * 40)
        print(f"{'Kode':<8} {'Nama Obat':<18} {'Stok':<6} {'Harga':>6}")
        print("-" * 40)
        
        found_index = -1
        kode_hapus = input("Masukkan KODE OBAT yang ingin dihapus: ").upper().strip()
        
        for i, obat in enumerate(data_obat):
            if obat[0] == kode_hapus:
                found_index = i
                break
            
        if found_index == -1:
            print(f"Kode obat '{kode_hapus}' tidak ditemukan.")
        else:
            obat_dihapus = data_obat.pop(found_index)
            print(f"\nObat '{kode_hapus[1]}' berhasil dihapus dari daftar")
            
    elif opsi == '5':
        current_role = None
        print("Logout berhasil")
        break
    
    else:
        print("Pilihan tidak valid. Mohon masukkan angka 1 sampai 5.")
        