import os

data_mahasiswa = ["Ifnu", "Adi", "ucup", "michael"]

def clear():
    os.system('cls || clear')

def tampilkan_mahasiswa():
    hasil = ""
    for i in range(len(data_mahasiswa)):
        hasil += f"data ke {i+1}\n"
        hasil += f"Nama : {data_mahasiswa[i]}\n"
        hasil += "="*10 + "\n"
    return hasil

def tambah_data():
    print("MENU TAMBAH DATA")
    print("=" * 10)
    inputUser = input("Data yang mau ditambahkan : ")
    data_mahasiswa.append(inputUser)
    return f"{inputUser} telah ditambahkan"

def ubah_data():
    tampilkan_mahasiswa()
    index = int(input("masukkan index yang mau diedit : "))
    data_baru = input("masukkan nama anda :")
    data_mahasiswa[index-1] = data_baru
    return "data berhasil diubah"

def hapus_data():
    tampilkan_mahasiswa()
    index_user = int(input("masukkan index yang ingin dihapus: "))
    del_user = data_mahasiswa.pop(index_user-1)
    return f"{del_user} telah dihapus"

def menu():
    return """
    Menu
Lihat Data  >> 1
Tambah Data >> 2
Edit Data   >> 3
Hapus Data  >> 4
Keluar      >> 5
"""

while True:
    print(menu())
    pilih = input("Masukan Pilihan menu >> ")
    clear()
    
    if pilih == "1":
        print("===Lihat Data===")
        print(tampilkan_mahasiswa())
        input("Enter.....")
        clear()
    elif pilih == "2":
        hasil = tambah_data()
        print(hasil)
        input("Enter....")
        clear()
    elif pilih == "3":
        print("Menu ubah data")
        hasil = ubah_data()
        print(hasil)
        input("Enter.....")
        clear()
    elif pilih == "4":
        print("Menu Hapus Data")
        hasil = hapus_data()
        print(hasil)
        input("Enter......")
        clear()
    elif pilih == "5":
        print("Anda memilih menu 5")
        break
    else:
        print(f"Menu {pilih} tidak tersedia")
        input("Enter.....")
        clear()