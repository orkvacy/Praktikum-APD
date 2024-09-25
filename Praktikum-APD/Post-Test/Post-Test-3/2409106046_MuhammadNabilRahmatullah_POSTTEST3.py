import math
import os

# bersihin terminal
clear = lambda: os.system('cls')

while True:
    clear()
    print("=====================================================")
    print("\t\tKalkulator Bangun Ruang")
    print("=====================================================")
    print("1. Kubus\n2. Balok\n3. Silinder\n0. Keluar")

    bangunRuang = int(input("Pilih Jenis Bangun Ruang : "))

    if bangunRuang == 0:
        print("Terima kasih telah menggunakan Kalkulator Bangun Ruang!")
        break

    elif bangunRuang == 1:
        clear()
        print("=================================================")
        print("          Apa yang Mau Kamu Hitung")
        print("=================================================")
        print("1. Volume Kubus\n2. Luas Permukaan Kubus\n3. Diagonal Kubus")
        kubus = int(input("Masukkan Angka : "))
        clear()
        if kubus == 1:  #rumus eksekusi
            sisiKubus = float(input("Masukkan Panjang Sisinya (dalam cm) : "))
            print(f"Volume Kubus Adalah : {sisiKubus ** 3:.2f} cm\u00B3")
        elif kubus == 2:
            luasPkubus = float(input("Masukkan Panjang Sisinya (dalam cm) : "))
            print(f"Luas Permukaan kubus adalah : {6 * (luasPkubus ** 2):.2f} cm\u008B2")
        elif kubus == 3:
            diagonalKubus = float(input("Masukkan Panjang Sisi Kubus (dalam cm) : "))
            print(f"Diagonal Kubus yaitu : {diagonalKubus * math.sqrt(3):.2f}")
        else:
            print("Maaf Pilihan Ini Tidak Tersedia")

    elif bangunRuang == 2:
        clear()
        print("===================================================")
        print("            Apa yang Mau Kamu Hitung")
        print("===================================================")
        print("1. Volume Balok\n2. Luas Permukaan Balok")
        balok = float(input("Masukkan Angka : "))
        clear()
        if balok == 1:
            panjangBalok = float(input("Masukkan Panjang Balok (dalam cm) : "))
            lebarBalok = float(input("Masukkan Lebar Baloknya (dalam cm) : "))
            tinggiBalok = float(input("Masukkan Tinggi baloknya (dalam cm) : "))
            print(f"Volume Balok Adalah : {panjangBalok * lebarBalok * tinggiBalok:.2f} cm\u00B3")
        elif balok == 2:
            panjangBalok = float(input("Masukkan Panjang Balok (dalam cm) : "))
            lebarBalok = float(input("Masukkan Lebar Baloknya (dalam cm) : "))
            tinggiBalok = float(input("Masukkan Tinggi baloknya (dalam cm) : "))
            print(f"Luas Permukaan Balok adalah : {2 * (panjangBalok * lebarBalok + panjangBalok * tinggiBalok + lebarBalok * tinggiBalok):.2f} cm\u00B2")
        else:
            print("Maaf Pilihan Ini Tidak Tersedia")

    elif bangunRuang == 3:
        clear()
        print("=========================================")
        print("        Apa yang Mau Kamu Hitung")
        print("=========================================")
        print("1. Volume Silinder\n2. Keliling Alas Silinder")
        silinder = int(input("Masukkan Angka: "))
        clear()
        if silinder == 1: #eksekusi
            jariSilinder = float(input("Masukkan Panjang jari-jarinya (dalam cm) : "))
            tinggiSilinder = float(input("Masukkan Tinggi Silinder (dalam cm) : "))
            print(f"Volume Silinder Adalah : {math.pi * jariSilinder**2 * tinggiSilinder:.2f} cm\u00B3")
        elif silinder == 2:
            jariSilinder = float(input("Masukkan Panjang Sisinya (dalam cm) : "))
            print(f"Keliling Alas Silinder adalah : {2 * math.pi * jariSilinder:.2f} cm")
        else:
            print("Maaf Pilihan Ini Tidak Tersedia")

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    input("\nTekan Enter untuk kembali ke menu utama...")