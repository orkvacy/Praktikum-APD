import sys
import time
from login import login, register, clear
from sistem import adminMenu, userMenu

def main():
    while True:
        clear()
        print("-" * 11, "Main Menu", "-" * 11, "\n1. Login\n2. Register\n0. Keluar")
        
        pilih = input("\nPilih Menu: ")
        
        if pilih == "1":
            user = login()
            if user:
                if user[2] == "admin":
                    adminMenu()
                else:
                    userMenu(user[0])
        elif pilih == "2":
            register()
        elif pilih == "0":
            clear()
            kalimat = "Terimakasih sudah menggunakan Sistem kami:)\n\tHave a nice day!"
            for kalimat in kalimat:
                sys.stdout.write(kalimat)
                time.sleep(0.03)
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
