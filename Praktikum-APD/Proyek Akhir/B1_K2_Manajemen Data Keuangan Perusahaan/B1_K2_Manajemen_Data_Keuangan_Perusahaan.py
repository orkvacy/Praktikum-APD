import os #buat clear
import pandas as pd #buat manipulasi data
import time #buat jeda waktu
import sys #untuk mengubah runtime
from datetime import datetime #buat nambahin tanggal,bulan,hari
import matplotlib.pyplot as plt #buat visualisasi data
from auth import register, login  #ambil fungsi register dan login dari file auth
from admin import adminMenu, midPrint, clear #ambil fungsi adminMenu, midPrint, dan clear dari file admin
from sales import salesMenu #ambil fungsi salesMenu dari file sales
from colorama import Fore, Style #buat warna



def mainMenu():
    width = 50  #lebar
    while True:
        clear()
        # Header
        print(Fore.CYAN + Style.BRIGHT + "=" * width)
        print(midPrint("=== SISTEM MANAJEMEN RETAIL ===", width))
        print("=" * width + Style.RESET_ALL)
        print("|" + " " * (width - 2) + "|")
        print("|" + midPrint("1. Login", width - 2) + "|")
        print("|" + midPrint("2. Register", width - 2) + "|")
        print("|" + midPrint("0. Keluar", width - 2) + "|")
        print("|" + " " * (width - 2) + "|")
        print("=" * width)

        choice = input(Fore.YELLOW + Style.BRIGHT + "Pilih menu: " + Style.RESET_ALL)
        
        if choice == "1":
            user = login()
            if user is not None:
                if user['role'] == 'admin':
                    adminMenu(user['username'])
                else:
                    salesMenu(user['username'])
        elif choice == "2":
            register()
        elif choice == "0":
            kalimat = """Terimakasih telah menggunakan program!\n⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣴⣦⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⠾⠛⠉⠉⠀⠀⠀⠀⠈⠉⠛⠿⣦⣄⠀⠀⠀⠀⠀
⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀
⠀⣰⡟⠁⠀⠀⠀⣀⡤⡀⠀⠀⠀⠀⠀⣠⢄⠀⠀⠀⠀⠻⣧⠀⠀
⣰⡟⠀⠀⠀⠀⢰⣿⣿⣷⠀⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⠀⢻⣧⠀
⣿⠃⠀⠀⠀⠀⠘⣿⣿⡿⠀⠀⠀⠀⢹⣿⣿⠇⠀⠀⠀⠀⠈⣿⡄
⣿⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⣿⡇
⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃
⠹⣧⠀⠀⠀⢳⣤⣄⣀⡀⠀⠀⠀⠀⠀⣀⣀⣤⡾⠀⠀⠀⣸⡟⠀
⠀⠻⣧⡀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣴⡟⠀⠀
⠀⠀⠙⢷⣄⡀⠀⠈⠛⠿⣿⣿⣿⣿⠿⠟⠋⠀⠀⣠⣾⠏⠀⠀⠀
⠀⠀⠀⠀⠙⠻⣶⣤⣀⡀⠀⠀⠀⠀⠀⣀⣠⣴⠿⠋⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠿⠿⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠀⠀⠂⠀⠀⠀⠀\nHave a nice day!"""
            for _ in kalimat:
                sys.stdout.write(_) #menulis perhuruf
                time.sleep(0.005) #jeda penulisan perhuruf
            break
        else:
            input("Menu tidak valid! Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    mainMenu()
