nama = input("Masukkan Nama: ")
umur = int(input("Masukkan Umur: "))
tinggiBadan = float(input("Masukkan Tinggi Badan (dalam cm): "))
beratBadan = float(input("Masukkan Berat Badan (dalam kg): "))
statusMahasiswa = input("Apakah Anda Mahasiswa Aktif? (aktif/tidak): ").lower()

#  untuk ngitung jumlah Variable
jumlah_numerik = [umur, tinggiBadan, beratBadan]

total = 0

for variabel in jumlah_numerik:
    if isinstance(variabel, (int, float)):
        total += variabel

print("\n=========================")
print("       Bio Data Anda      ")
print("=========================")
print(f"Nama               : {nama}")
print(f"Umur               : {umur}")
print(f"Tinggi Badan       : {tinggiBadan} cm")
print(f"Berat Badan        : {beratBadan} kg")
print(f"Mahasiswa Aktif    : {'Aktif' if statusMahasiswa == 'aktif' else 'Tidak Aktif'}")
print("=========================")
print(f"Total variabel numerik (int/float): {total:.3f}")
print("=========================")
