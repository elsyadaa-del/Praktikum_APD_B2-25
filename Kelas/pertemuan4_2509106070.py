# #perulangan
# for i in range (1, 10):
#     print(f'perulangan ke {i}')

# # angka pertama adalah start, kedua adalah stop, ketiga adalah step (melangkah)
# for i in range (1, 10, 3):
#     print(f'perulangan ke {i}')

# #for pada list
# mahasiswa = ["ahnap", "dapupu", 10, "jarvis"]
# for i in mahasiswa :0
#     print(i)

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("#", end="*")
#     print ("")

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi? ")
print(f"Total perulangan: {hitung}")

# angka = [2, 5, 8, 12, 15, 7, 20]
# print("Mencari angka pertama yang lebih besar dari 10...")
# for n in angka:
#     print(f"Sekarang memeriksa angka: {n}")
#     if n > 10:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#         break
# print("Program selesai.")

while True:
    print ("Menu")
    print ("1. Fitur 1")
    print ("2. Fitur 2")
    opsi = int(input("Masukkan opsi: "))
    if opsi == 1:
        print ("1.Fitur 1")
    elif opsi == 2:
        print ("2. Fitur 2")
    elif opsi == 3:
        break