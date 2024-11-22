import pandas as pd
from getpass import getpass #import untuk input password
from colorama import Fore, Style, init
from admin import load
import re

def register():
    try:
        try:
            print("\n=== REGISTER ===")
            username = input("Username: (3-10 Karakter) ")
            if len(username) < 3: #jika username kurang dari 3 karakter akan terjadi nerror
                raise ValueError(Fore.RED + "Username minimal 3 karakter")
            if len(username) > 10: #jika username lebih dari 10 karakter akan terjadi error
                raise ValueError(Fore.RED + "Username maximal 10 karakter.")
            if not username: #agar username tidak bisa kosong atau hanya input spasi
                raise ValueError(Fore.RED + "Username tidak boleh kosong!" + Style.RESET_ALL)
            if not re.match("^[A-Za-z0-9]*$", username): #username hanya boleh berisi karakter a-z, A-Z, 0-9
                raise ValueError(Fore.RED + "Username hanya boleh mengandung huruf dan angka tanpa karakter spesial!" + Style.RESET_ALL)
            
            try:
                userDF = pd.read_csv('user.csv') #membaca file user.csv
            except FileNotFoundError: #jika file tidak ditemukan maka terjadi error (tidak menghentikan program)
                print(Fore.RED + "Error: File 'user.csv' tidak ditemukan. Pastikan file tersedia." + Style.RESET_ALL)
                return
            
            if username in userDF['username'].values: #melakukan pengecekan apakah username sudah digunakan sebelumnya
                input("Username sudah terdaftar! Tekan Enter untuk melanjutkan...")
                return
            
            password = getpass("Password: (3-10 Karakter)") #agar pada saat melakukan input tidak terlihat di terminal
            if len(password) < 3:
                raise ValueError(Fore.RED + "Password minimal 3 karakter")
            if len(password) > 10:
                raise ValueError(Fore.RED + "Password maximal 10 karakter.")
            if not password:
                raise ValueError("Password tidak boleh kosong!")
            if not re.match("^[A-Za-z0-9]*$", password): #password hanya boleh berisi karakter a-z, A-Z, 0-9
                raise ValueError(Fore.RED + "Password hanya boleh mengandung huruf dan angka tanpa karakter spesial!" + Style.RESET_ALL)
            print("\nPilih role:")
            print("1. Admin")
            print("2. Sales")
            inputRole = input("Pilih role : ")

            if inputRole == "1":
                autentikasi = getpass("Masukkan kode autentikasi admin: ") 
                if autentikasi != "admin123":  #jika kode selain ini maka kode dinyatakan tidak valid
                    input(Fore.RED + "Kode rahasia salah! Tekan Enter untuk kembali ke menu utama..." + Style.RESET_ALL)
                    return
                role = "admin" #jika kode benar maka akan diberi role sebagai admin
            elif inputRole == "2":
                role = "Sales"
            else:
                input(Fore.RED + "Pilihan role tidak valid! Tekan Enter untuk kembali ke menu utama..." + Style.RESET_ALL)
                return

            if username and password and role:
                userBaru = pd.DataFrame([[username, password, role]], columns=["username", "password", "role"]) #membuat variabel data baru
                userDF = pd.concat([userDF, userBaru], ignore_index=True) #menggabungkan data baru
                userDF.to_csv('user.csv', index=False)  #simpan data pengguna baru ke file user.csv

            if role == "Sales": #menambahkan target dan bonus secara otomatis jika memilih role sales
                try:
                    salesDF = pd.read_csv('sales.csv')
                except FileNotFoundError:
                    salesDF = pd.DataFrame(columns=["username", "target", "bonus"])
                
                salesBaru = pd.DataFrame([[username, 1000000, 100000]], columns=["username", "target", "bonus"])
                salesDF = pd.concat([salesDF, salesBaru], ignore_index=True)
                salesDF.to_csv('sales.csv', index=False)
            
            print(Fore.GREEN + "Registrasi berhasil!" + Style.RESET_ALL)
        
        except ValueError as e:
            print(Fore.RED + f"Input Error: {e}" + Style.RESET_ALL)
        input("Tekan Enter untuk melanjutkan")
    except EOFError:
        print(Fore.RED + "Anda terindikasi menekan CTRL+Z" + Style.RESET_ALL)
        input("Tekan Enter untuk melanjutkan")


def login(): #fungsi login
    kesempatan = 3
    while kesempatan > 0:
    
        try:
            print("\n=== LOGIN ===")
            username = input("Username: ")
            if not username:
                raise ValueError(Fore.RED + "Username tidak boleh kosong!" + Style.RESET_ALL)
            if not re.match("^[A-Za-z0-9]*$", username):
                raise ValueError(Fore.RED + "Username hanya boleh mengandung huruf dan angka tanpa karakter spesial!" + Style.RESET_ALL)
            password = getpass("Password: ")
            if not password:
                raise ValueError(Fore.RED + "Password tidak boleh kosong" + Style.RESET_ALL)
            userDF =pd.read_csv('user.csv')
            user = userDF[(userDF['username'] == username) & (userDF['password'] == password)]
            
            if not user.empty:
                print(Fore.GREEN + "\nLogin berhasil! Tunggu sebentar" + Style.RESET_ALL)
                load()
                return {'username': username, 'role': user.iloc[0]['role']}
            else:
                kesempatan -= 1
                print(Fore.RED + f"Username atau password salah! Kesempatan login tersisa {kesempatan}" + Style.RESET_ALL)
                
                if kesempatan == 0:
                    print("Kesempatan habis, anda akan keluar dari program")
                    exit()
            
        except ValueError as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)
        input("Tekan enter untuk melanjutkan....")
