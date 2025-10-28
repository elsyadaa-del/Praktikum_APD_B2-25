# -- DATA GLOBAL --
user_data = {
    "apoteker" : {"password": "1234", "role": "apoteker"},
    "user": {"password": "2345", "role": "user"}
}
obat_data = {
    101: {"nama": "Paracetamol", "stok": 50, "harga": 5000},
    102: {"nama": "Amoxicillin", "stok": 30, "harga": 15000},
    103: {"nama": "Komix", "stok": 20, "harga": 10000},
    104: {"nama": "OBH", "stok": 15, "harga": 13000},
    105: {"nama": "Tremenza", "stok": 20, "harga": 20000},
    106: {"nama": "Omeprazol", "stok": 13, "harga": 15000}
}
next_kode_obat = 107 
pengguna = None 
role_pengguna = None  
run = True
def get_int_input(pilihan_opsi, min_nilai, max_nilai):
    while True:
        input_str = input(pilihan_opsi).strip()
        if not input_str:
            print("Input tidak boleh kosong.")
            continue
        try:
            pilihan = int(input_str)
            if min_nilai <= pilihan <= max_nilai:
                return pilihan
            else:
                print(f"Opsi tidak valid. Pilih antara {min_nilai} dan {max_nilai}.")
        except ValueError:
            print("Input harus berupa angka.")

def tampilkan_daftar_obat_user():
    output = ""
    print( "\n--- Daftar Obat ---\n")
    if not obat_data:
        output += "Data obat kosong."
    else:
        for kodeObat, data in obat_data.items():
            output += f"Kode: {kodeObat} | Nama: {data['nama']} | Harga: {data['harga']} | Stok: {data['stok']}\n"
    print(output)
    return True

def proses_pembelian(kode_obat, jumlah_beli):
    if kode_obat not in obat_data:
        print("Kode obat tidak valid.")
        return False
    
    data_obat = obat_data[kode_obat]
    nama_obat = data_obat['nama']
    harga_satuan = data_obat['harga']

    if jumlah_beli <= 0:
        print("Jumlah beli harus positif.")
        return False
        
    if data_obat['stok'] < jumlah_beli:
        print(f"Stok {nama_obat} tidak mencukupi (Tersedia: {data_obat['stok']}).")
        
        
        def minta_jumlah_ulang(nama_obat, max_stok):
            print(f"Mohon masukkan ulang jumlah pembelian untuk {nama_obat}. Maksimal {max_stok}.")
            try:
                jumlah_baru_str = input("Jumlah Beli Baru (0 untuk batal): ").strip()
                if not jumlah_baru_str:
                    return minta_jumlah_ulang(nama_obat, max_stok)
                jumlah_baru = int(jumlah_baru_str)
                if jumlah_baru == 0:
                    print("Pembelian dibatalkan.")
                    return 0
                elif jumlah_baru < 0:
                    print("Jumlah tidak boleh negatif.")
                    return minta_jumlah_ulang(nama_obat, max_stok)
                elif jumlah_baru > max_stok:
                    print(f"Jumlah melebihi stok tersedia ({max_stok}).")
                    return minta_jumlah_ulang(nama_obat, max_stok) 
                else:
                    return jumlah_baru
            except ValueError:
                print("Input harus berupa angka.")
                return minta_jumlah_ulang(nama_obat, max_stok)

        jumlah_beli_baru = minta_jumlah_ulang(nama_obat, data_obat['stok'])
        if jumlah_beli_baru == 0:
            return False
        jumlah_beli = jumlah_beli_baru

    # Lakukan Transaksi
    data_obat['stok'] -= jumlah_beli
    total_harga = jumlah_beli * harga_satuan
    print(f"\nPembelian berhasil:")
    print(f"- Obat: {nama_obat}")
    print(f"- Jumlah: {jumlah_beli}")
    print(f"- Total Harga: {total_harga:,}")
    return True
    
    
# Cek ketersediaan data obat
def cek_obat_kosong():
    global obat_data
    return not obat_data

# Menampilkan Daftar Obat Lengkap
def prosedur_tampilkan_obat_admin():
    if cek_obat_kosong():
        print("Data obat kosong.")
        return
        
    print("\n--- Daftar Obat (Admin) ---")
    for kodeObat, data in obat_data.items():
        print(f"Kode: {kodeObat} | Nama: {data['nama']} | Stok: {data['stok']} | Harga: {data['harga']:,}")

# Proses Tambah Obat Baru
def prosedur_tambah_obat_baru():
    global next_kode_obat, obat_data
    print("\n--- Tambah Obat Baru ---")
    
    nama = input("Nama Obat: ").strip()
    if not nama:
        print("Nama obat tidak boleh kosong. Penambahan dibatalkan.")
        return

    # Validasi Stok
    while True:
        try:
            stok = int(input("Stok: ").strip())
            if stok >= 0:
                break
            else:
                print("Stok tidak boleh negatif.")
        except ValueError:
            print("Stok harus berupa angka.")

    # Validasi Harga
    while True:
        try:
            harga = int(input("Harga: ").strip())
            if harga >= 0:
                break
            else:
                print("Harga tidak boleh negatif.")
        except ValueError:
            print("Harga harus berupa angka.")
            
    obat_data[next_kode_obat] = {"nama": nama, "stok": stok, "harga": harga}
    print(f"Obat '{nama}' berhasil ditambahkan dengan kode {next_kode_obat}.")
    next_kode_obat += 1

while run:
    if pengguna is None:
        # --- MENU PRE-LOGIN ---
        print("\n=== Selamat Datang di Toko Obat Sehat ===")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        
        pilihan = get_int_input("Pilih Opsi (1-3): ", 1, 3) 
        
        if pilihan == 1:
            # --- Login ---
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            if username in user_data:
                if user_data[username]["password"] == password:
                    pengguna = username
                    role_pengguna = user_data[username]["role"]
                    print(f"Login berhasil! Selamat datang, {username} ({role_pengguna}).")
                    continue
                else:
                    print("Password salah.") 
            else:
                print("Username tidak ditemukan.")
                
        elif pilihan == 2:
            # --- Registrasi ---
            print("\n--- Registrasi Pengguna Baru ---")
            new_username = input("Masukkan Username Baru: ").strip()
            new_password = input("Masukkan Password: ").strip()
            
            if not new_username or not new_password:
                print("Username dan Password tidak boleh kosong.")
            elif new_username in user_data:
                print("Username sudah terdaftar.")
            else:
                if len(new_password) < 4:
                    print("Password minimal 4 karakter.")
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
            print(f"\n=== Menu Admin ({pengguna}) ===")
            print("1. Lihat Daftar Obat")
            print("2. Tambah Obat Baru")
            print("3. Perbarui Stok/Harga Obat")
            print("4. Hapus Obat")
            print("5. Logout")
            
            opsi_menu = get_int_input("Pilih Opsi (1-5): ", 1, 5)
                
            # pilihan Menu Admin
            if opsi_menu == 1:
                prosedur_tampilkan_obat_admin()

            elif opsi_menu == 2:
                prosedur_tambah_obat_baru()

            elif opsi_menu == 3:
                # Memperbarui obat 
                print("\n--- Perbarui Obat ---")
                
                # Input Kode Obat
                kodeObat = None
                while True:
                    inputKode = input("Masukkan kode obat yang akan diubah: ").strip()
                    try:
                        kodeObat = int(inputKode)
                        break
                    except ValueError:
                        print("Kode obat harus berupa angka.")
                        
                if kodeObat in obat_data:
                    print(f"Obat yang dipilih: {obat_data[kodeObat]['nama']}")
                    
                    stok_baru_str = input("Masukkan Stok Baru (kosongkan jika tidak diubah): ").strip()
                    harga_baru_str = input("Masukkan Harga Baru (kosongkan jika tidak diubah): ").strip()

                    updated = False
                    
                    # Cek dan update stok
                    if stok_baru_str:
                        try:
                            stokBaru = int(stok_baru_str)
                            if stokBaru >= 0:
                                obat_data[kodeObat]['stok'] = stokBaru
                                updated = True
                            else:
                                print("Stok tidak boleh negatif. Perubahan stok dibatalkan.")
                        except ValueError:
                            print("Stok harus berupa angka. Perubahan stok dibatalkan.")

                    # Cek dan update harga 
                    if harga_baru_str:
                        try:
                            hargaBaru = int(harga_baru_str)
                            if hargaBaru >= 0:
                                obat_data[kodeObat]['harga'] = hargaBaru
                                updated = True
                            else:
                                print("Harga tidak boleh negatif. Perubahan harga dibatalkan.")
                        except ValueError:
                            print("Harga harus berupa angka. Perubahan harga dibatalkan.")
                            
                    if updated:
                        print(f"Kode obat {kodeObat} berhasil diperbarui.")
                    elif not stok_baru_str and not harga_baru_str:
                        print("Tidak ada perubahan dilakukan.")
                else:
                    print(f"Kode obat {kodeObat} tidak ditemukan.")

            elif opsi_menu == 4:
                # Menghapus obat
                print("\n--- Hapus Obat ---")
                
                kodeObat = None
                while True:
                    inputKode = input("Masukkan kode obat yang akan dihapus: ").strip()
                    try:
                        kodeObat = int(inputKode)
                        break
                    except ValueError:
                        print("Kode obat harus berupa angka.")
                
                if kodeObat in obat_data:
                    nama_obat_hapus = obat_data[kodeObat]['nama']
                    del obat_data[kodeObat]
                    print(f"Obat '{nama_obat_hapus}' (Kode {kodeObat}) berhasil dihapus.")
                else:
                    print(f"Kesalahan: Kode obat {kodeObat} tidak ditemukan.")

            # 5. Logout
            elif opsi_menu == 5:
                print(f"Pengguna {pengguna} berhasil logout.")
                pengguna = None
                role_pengguna = None

        elif role_pengguna == "user":
            # --- MENU USER BIASA ---
            print(f"\n=== Menu Pengguna ({pengguna}) ===")
            print("1. Lihat Daftar Obat")
            print("2. Beli Obat")
            print("3. Logout")
            
            opsi_menu = get_int_input("Pilih Opsi (1-3): ", 1, 3)

            # Pilihan Menu User
            if opsi_menu == 1:
                tampilkan_daftar_obat_user()
                
            elif opsi_menu == 2:
                # --- BELI OBAT ---
                if cek_obat_kosong():
                    print("\nTidak ada obat yang tersedia untuk dibeli.")
                    continue
                    
                tampilkan_daftar_obat_user() 
                print("\n--- Proses Pembelian Obat ---")
                
                kodeObat = None
                while True:
                    inputKode = input("Masukkan kode obat yang akan dibeli: ").strip()
                    try:
                        kodeObat = int(inputKode)
                        if kodeObat in obat_data:
                            break
                        else:
                            print("Kode obat tidak ditemukan.")
                    except ValueError:
                        print("Kode obat harus berupa angka.")
                        
                jumlahBeli = None
                while True:
                    inputJumlah = input(f"Masukkan jumlah beli {obat_data[kodeObat]['nama']}: ").strip()
                    try:
                        jumlahBeli = int(inputJumlah)
                        break
                    except ValueError:
                        print("Jumlah beli harus berupa angka.")
                proses_pembelian(kodeObat, jumlahBeli)
                
            # 3. Logout
            elif opsi_menu == 3:
                print(f"Pengguna {pengguna} berhasil logout.")
                pengguna = None
                role_pengguna = None