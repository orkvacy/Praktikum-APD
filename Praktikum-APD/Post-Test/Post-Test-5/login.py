import os
import time
from data import users

def clear():
    os.system('cls || clear')

def login():
    clear()
    print("=" * 25, "LOGIN", "=" * 25)
    username = input("Username: ")
    password = input("Password: ")
    
    for user in users:
        if user[0] == username and user[1] == password:
            return user
    
    print("Username atau password salah! Kembali ke menu utama.")
    input("Tekan Enter untuk melanjutkan...")
    return None

def register():
    try:
        clear()
        print("=" * 25, "REGISTER", "=" * 25)
        username = input("Username baru: ")
        
        if any(user[0] == username for user in users):
            print("Username sudah digunakan!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        password = input("Password: ")
        users.append([username, password, "user"])
        print("Succes!")
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")
