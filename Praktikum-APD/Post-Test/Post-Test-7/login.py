import os
from data import users

def clear():
    os.system('cls || clear')

def login():
    clear()
    print("=" * 25, "LOGIN", "=" * 25)
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users and users[username]["password"] == password:
        return {
            "username": username,
            "password": users[username]["password"],
            "role": users[username]["role"]
        }
    
    print("Username atau password salah! Kembali ke menu utama.")
    input("Tekan Enter untuk melanjutkan...")
    return None

def register():
    try:
        clear()
        print("=" * 25, "REGISTER", "=" * 25)
        username = input("Username baru: ")
        
        if username in users:
            print("Username sudah digunakan!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        password = input("Password: ")
        users[username] = {"password": password, "role": "user"}
        print("Succes!")
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")
