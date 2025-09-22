# input sata dari pengguna

nama = input("Silahkan isi nama anda..")
NIM = int(input("Silahkan isi NIM anda.."))
harga = int(input("Budget yang inginkan.."))
 # hitung harga makanan + PPN 
hpl = 15000 + (15000 * 5/100)   # Pecel Lele + 5% PPN
hma = 15000 + (15000 *8/100)    #Mie Ayam + 8% PPN
hnp = 15000 + (15000 *10/100)   # Nasi Padang + 10% PPN
 #Tampilkan hasil
 
print("\nDaftar Harga Makanan (sudah termasuk PPN):")
print(f"Harga Pecel Lele: Rp {int(hpl)}")
print(f"Harga Mie Ayam  : Rp {int(hma)}")
print(f"Harga Nasi Padang: Rp {int(hnp)}")
print("\nHarga sudah termasuk dengan PPN.")