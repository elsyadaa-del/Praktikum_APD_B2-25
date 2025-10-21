# --- DATA LOGIN ---
user_data = {
    "apoteker": {"password": "123", "role": "apoteker"},
    "user": {"password": "234", "role": "user"}
}
#--- DATA OBAT ---
obat_data = {
    101: {"nama": "Paracetamol", "stok": 50, "harga": 5000},
    102: {"nama": "Amoxicillin", "stok": 30, "harga": 15000}
}
next_kode_obat = 103
pengguna = None  
role_pengguna = None 
run = True

while run:
    if pengguna is None:
        # --- MENU PRE-LOGIN ---
        print("\n=== Selamat Datang di Toko Obat Sehat ===")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        
        # Inisiasi pilihan untuk menu
        pilihan = None 
        is_input_valid = False
        
        while not is_input_valid:
            user_input = input("Pilih Opsi (1-3): ").strip()
            if not user_input:
                print("Input tidak boleh kosong.")
                continue
            
            if user_input.isdigit():
                pilihan = int(user_input)
                if 1 <= pilihan <= 3:
                    is_input_valid = True
                else:
                    print("Opsi tidak valid. Pilih 1, 2, atau 3.")
            else:
                print("Input harus berupa angka.")
                
        if pilihan == 1:
            # --- Login ---
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            if username in user_data:
                if user_data[username]["password"] == password:
                    pengguna = username
                    role_pengguna = user_data[username]["role"]
                    print(f"Login berhasil! Selamat datang, {username} ({role_pengguna}).")
                else:
                    print("Kesalahan: Password salah.") 
            else:
                print("Kesalahan: Username tidak ditemukan.")
                
        elif pilihan == 2:
            # --- Registrasi ---
            print("\n--- Registrasi Pengguna Baru ---")
            new_username = input("Masukkan Username Baru: ").strip()
            new_password = input("Masukkan Password: ").strip()
            
            if not new_username or not new_password:
                print("Kesalahan: Username dan Password tidak boleh kosong.")
            elif new_username in user_data:
                print("Kesalahan: Username sudah terdaftar.")
            else:
                user_data[new_username] = {"password": new_password, "role": "user"}
                print(f"Registrasi {new_username} berhasil. Silakan Login.")
                
        elif pilihan == 3:
            # --- Keluar Program ---
            run = False
            print("Terima kasih, program diakhiri.")
            
    elif pengguna is not None:
        if role_pengguna == "apoteker":
            # --- MENU ADMIN (Apoteker) ---
            print("\n=== Menu Admin (Apoteker) ===")
            print("1. Lihat Daftar Obat")
            print("2. Tambah Obat Baru")
            print("3. Perbarui Stok/Harga Obat")
            print("4. Hapus Obat")
            print("5. Logout")
            
            opsi_menu = None
            input_valid = False
            while not input_valid:
                user_input = input("Pilih Opsi (1-5): ").strip()
                if user_input.isdigit():
                    opsi_menu = int(user_input)
                    if 1 <= opsi_menu <= 5:
                        input_valid = True
                    else:
                        print("Opsi tidak valid. Pilih 1 sampai 5.")
                else:
                    print("Input harus berupa angka.")
                    
                    
            # pilihan Menu Admin
            if opsi_menu == 1:
                print("\n--- Daftar Obat ---")
                if not obat_data:
                    print("Data obat kosong.")
                else:
                    for kodeObat, data in obat_data.items():
                        print(f"Kode: {kodeObat} | Nama: {data['nama']} | Stok: {data['stok']} | Harga: {data['harga']}")

            elif opsi_menu == 2:
                # tambah obat
                print("\n--- Tambah Obat Baru ---")
                nama = input("Nama Obat: ").strip()
                #tambah stok
                stok = -1
                while True:
                    stok_input = input("Stok (angka): ").strip()
                    if stok_input.isdigit():
                        stok = int(stok_input)
                        if stok >= 0:
                            break
                        else:
                            print("Stok tidak boleh negatif.")
                    else:
                        print("Stok harus berupa angka.")
                #tambah harga
                harga = -1
                while True:
                    harga_input = input("Harga (angka): ").strip()
                    if harga_input.isdigit():
                        harga = int(harga_input)
                        if harga >= 0:
                            break
                        else:
                            print("Harga tidak boleh negatif.")
                    else:
                        print("Harga harus berupa angka.")
                            
                if nama:
                    obat_data[next_kode_obat] = {"nama": nama, "stok": stok, "harga": harga}
                    print(f"Obat '{nama}' berhasil ditambahkan dengan kode {next_kode_obat}.")
                    next_kode_obat += 1
                else:
                    print("Nama obat tidak boleh kosong.")

            elif opsi_menu == 3:
                # memperbarui obat
                print("\n--- Perbarui Obat ---")
                
                # kode obat
                kodeObat = None
                while True:
                    inputKode = input("Masukkan kode obat yang akan diubah: ").strip()
                    if inputKode.isdigit():
                        kodeObat = int(inputKode)
                        break
                    else:
                        print("Kode obat harus berupa angka.")
                        
                if kodeObat in obat_data:
                    print(f"Obat yang dipilih: {obat_data[kodeObat]['nama']}")
                    
                    stok_baru_str = input("Masukkan Stok Baru (kosongkan jika tidak diubah): ").strip()
                    harga_baru_str = input("Masukkan Harga Baru (kosongkan jika tidak diubah): ").strip()

                    updated = False
                    
                    # Cek dan update stok
                    if stok_baru_str:
                        if stok_baru_str.isdigit():
                            stokBaru = int(stok_baru_str)
                            if stokBaru >= 0:
                                obat_data[kodeObat]['stok'] = stokBaru
                                updated = True
                            else:
                                print("Stok tidak boleh negatif.")
                        else:
                            print("Stok harus berupa angka. Perubahan stok dibatalkan.")

                    # Cek dan update harga 
                    if harga_baru_str:
                        if harga_baru_str.isdigit():
                            hargaBaru = int(harga_baru_str)
                            if hargaBaru >= 0:
                                obat_data[kodeObat]['harga'] = hargaBaru
                                updated = True
                            else:
                                print("Harga tidak boleh negatif.")
                        else:
                            print("Harga harus berupa angka. Perubahan harga dibatalkan.")
                            
                    if updated:
                        print(f"Kode obat {kodeObat} berhasil diperbarui.")
                    elif not stok_baru_str and not harga_baru_str:
                        print("Tidak ada perubahan dilakukan.")
                else:
                    print(f"Kode obat {kodeObat} tidak ditemukan.")

            elif opsi_menu == 4:
                # menghapus obat
                print("\n--- Hapus Obat ---")
                
                kodeObat = None
                while True:
                    inputKode = input("Masukkan kode obat yang akan dihapus: ").strip()
                    if inputKode.isdigit():
                        kodeObat = int(inputKode)
                        break
                    else:
                        print("kode obat harus berupa angka.")
                
                if kodeObat in obat_data:
                    del obat_data[kodeObat]
                    print(f"Kode obat {kodeObat} berhasil dihapus.")
                else:
                    print(f"Kesalahan: Kode obat {kodeObat} tidak ditemukan.")

            # 5. Logout
            elif opsi_menu == 5:
                print(f"Pengguna {pengguna} berhasil logout.")
                pengguna = None
                role_pengguna = None

        elif role_pengguna == "user":
            # --- MENU USER BIASA ---
            print("\n=== Menu Pengguna ===")
            print("1. Lihat Daftar Obat")
            print("2. Logout")
            
            opsi_menu = None
            input_valid = False
            
            # Pengambilan Input Menu User
            while not input_valid:
                user_input = input("Pilih Opsi (1-2): ").strip()
                if user_input.isdigit():
                    opsi_menu = int(user_input)
                    if 1 <= opsi_menu <= 2:
                        input_valid = True
                    else:
                        print("Opsi tidak valid. Pilih 1 atau 2.")
                else:
                    print("Input harus berupa angka.")

            # Logika Pilihan Menu User
            if opsi_menu == 1:
                print("\n--- Daftar Obat ---")
                if not obat_data:
                    print("Data obat kosong.")
                else:
                    for kodeObat, data in obat_data.items():
                        print(f"Kode: {kodeObat} | Nama: {data['nama']} | Stok: {data['stok']} | Harga: {data['harga']}")
            #logout
            elif opsi_menu == 2:
                print(f"Pengguna {pengguna} berhasil logout.")
                pengguna = None
                role_pengguna = None