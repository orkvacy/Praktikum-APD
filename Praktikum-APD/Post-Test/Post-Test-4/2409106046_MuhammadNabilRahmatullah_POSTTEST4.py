import os
import math
import time
import sys
clear = lambda: os.system('cls')


def load(panjangLoading=30, waktu=3.5):
    for i in range(panjangLoading + 1):
        time.sleep(waktu / panjangLoading)  
        bar = "=" * i + "-" * (panjangLoading - i)  
        print(f"\rLoading: [{bar}] {i * 100 // panjangLoading}%", end="")


def countdown(waktu=5, pesan="Anda akan kembali ke menu utama dalam"):
    for i in range(waktu, -1, -1):
        print(f"{pesan} {i} detik", end="\r")
        time.sleep(1)
    clear()



chance = 3
while chance > 0:
    clear()
    username = input("Masukkan username anda : ")
    password = input("Masukkan Password anda : ")
    if " " in username or " " in password or username == "" or password == "":
        print("Username atau Password tidak boleh menggunakan spasi atau input kosong")
        time.sleep(2)
        chance -= 1
        print(f"Kesempatan anda untuk login sisa {chance} kali")
        time.sleep(2)
        if chance == 0:
            print("Kesempatan Anda Habis")
            time.sleep(1)
            exit()
        continue
    if username == "nabil" and password == "046":
        print("Anda berhasil login\n Tunggu beberapa detik")
        load()
        break
    else:
        print("Username atau Password yang anda masukkan salah")
        chance -= 1
        print(f"Kesempatan anda untuk login sisa {chance} kali")
        time.sleep(2)
        if chance == 0:
            print("Kesempatan Anda Habis")
            time.sleep(1)
            exit()




while True:
    clear()
    print("=====================================================")
    print("\t\tKalkulator Bangun Ruang")
    print("=====================================================")
    print("1. Kubus\n2. Balok\n3. Silinder\n0. Keluar")

    bangunRuang = input("Pilih Jenis Bangun Ruang : ")

    if bangunRuang == "0":
        clear()
        kalimat = "Terimakasih telah menggunakan Kalkulator Bangun Ruang\n\t\tHave a Nice Day:)"
        for kalimat in kalimat:
                sys.stdout.write(kalimat) 
                time.sleep(0.04)  
        print()  
        break

    elif bangunRuang == "1":
        clear()
        print("=================================================")
        print("          Apa yang Mau Kamu Hitung")
        print("=================================================")
        print("1. Volume Kubus\n2. Luas Permukaan Kubus\n3. Diagonal Kubus")
        kubus = input("Masukkan Angka : ")
        clear()
        if kubus == "1":  #rumus eksekusi
            sisiKubus = float(input("Masukkan Panjang Sisinya (dalam cm) : "))
            print(f"Volume Kubus Adalah : {sisiKubus ** 3:.2f} cm\u00B3")
            countdown()
        elif kubus == "2":
            luasPkubus = float(input("Masukkan Panjang Sisinya (dalam cm) : "))
            print(f"Luas Permukaan kubus adalah : {6 * (luasPkubus ** 2):.2f} cm\u008B2")
            countdown()
        elif kubus == "3":
            diagonalKubus = float(input("Masukkan Panjang Sisi Kubus (dalam cm) : "))
            print(f"Diagonal Kubus yaitu : {diagonalKubus * math.sqrt(3):.2f}")
            countdown()
        else:
            print("Maaf Pilihan Ini Tidak Tersedia")
            countdown()

    elif bangunRuang == "2":
        clear()
        print("===================================================")
        print("            Apa yang Mau Kamu Hitung")
        print("===================================================")
        print("1. Volume Balok\n2. Luas Permukaan Balok")
        balok = input("Masukkan Angka : ")
        clear()
        if balok == "1":
            panjangBalok = float(input("Masukkan Panjang Balok (dalam cm) : "))
            lebarBalok = float(input("Masukkan Lebar Baloknya (dalam cm) : "))
            tinggiBalok = float(input("Masukkan Tinggi baloknya (dalam cm) : "))
            print(f"Volume Balok Adalah : {panjangBalok * lebarBalok * tinggiBalok:.2f} cm\u00B3")
            countdown()
        elif balok == "2":
            panjangBalok = float(input("Masukkan Panjang Balok (dalam cm) : "))
            lebarBalok = float(input("Masukkan Lebar Baloknya (dalam cm) : "))
            tinggiBalok = float(input("Masukkan Tinggi baloknya (dalam cm) : "))
            print(f"Luas Permukaan Balok adalah : {2 * (panjangBalok * lebarBalok + panjangBalok * tinggiBalok + lebarBalok * tinggiBalok):.2f} cm\u00B2")
            countdown()
        else:
            print("Maaf Pilihan Ini Tidak Tersedia")
            countdown()

    elif bangunRuang == "3":
        clear()
        print("=========================================")
        print("        Apa yang Mau Kamu Hitung")
        print("=========================================")
        print("1. Volume Silinder\n2. Keliling Alas Silinder")
        silinder = input("Masukkan Angka: ")
        clear()
        if silinder == "1": #eksekusi
            jariSilinder = float(input("Masukkan Panjang jari-jarinya (dalam cm) : "))
            tinggiSilinder = float(input("Masukkan Tinggi Silinder (dalam cm) : "))
            print(f"Volume Silinder Adalah : {math.pi * jariSilinder**2 * tinggiSilinder:.2f} cm\u00B3")
            countdown()
        elif silinder == "2":
            jariSilinder = float(input("Masukkan Panjang Sisinya (dalam cm) : "))
            print(f"Keliling Alas Silinder adalah : {2 * math.pi * jariSilinder:.2f} cm")
            countdown()
        else:
            print("Maaf Pilihan Ini Tidak Tersedia")
            countdown()

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        countdown = 5
        for i in range(countdown, -1, -1):
                print(f"Anda akan bisa kembali mengetik dalam {i} detik", end="\r")
                time.sleep(1)