import os #buat membersihkan terminal
import pandas as pd #manipulasi data
import matplotlib.pyplot as plt #buat grafik
import time #buat jeda waktu
import sys #untuk mengubah runtime
import re
from prettytable import PrettyTable #buat tabel
from datetime import datetime #buat tanggal
from colorama import Fore, Style, init #buat warna

def clear(): #buat clear terminal
    os.system('cls || clear')

def load(panjangLoading=30, waktu=3.5): #loading bar
    for i in range(panjangLoading + 1):
        time.sleep(waktu / panjangLoading)  
        bar = "=" * i + "-" * (panjangLoading - i)  
        print(f"\rLoading: [{bar}] {i * 100 // panjangLoading}%", end="")


def showPr(): #show produk
    clear()
    produkDF = pd.read_csv('produk.csv')
    if produkDF.empty:
        print(Fore.RED + "Belum ada produk." + Style.RESET_ALL)
        input("Tekan Enter untuk melanjutkan")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Nama produk", "Harga", "Stok"] #isi headers
        
        for _, row in produkDF.iterrows(): #baca tabel perbaris
            rupiah = f"Rp {row['harga']:,.2f}" #mengubah pada kolom Harga agar menjadi format Rupiah
            table.add_row([row['id'], row['nama'], rupiah, row['stok']])
        
        print(table)
        

def menuProduk(): #menuproduk
    clear()
    while True:
        clear()
        showPr()
        print("\n=== MENU PRODUK ===")
        print("1. Tambah Produk")
        print("2. Ubah Produk")
        print("3. Hapus Produk")
        print("0. Kembali")
        
        choice = input("Pilih menu: ")
        
        if choice == "1":
            tambahProduk()
        elif choice == "2":
            editPr()
        elif choice == "3":
            hapusPr()
        elif choice == "0":
            break
        else:
            input("Menu tidak valid! Tekan Enter untuk melanjutkan...")

def tambahProduk():
    try:
        produkDF = pd.read_csv('produk.csv') #membaca file csv
        print("\n=== TAMBAH PRODUK ===")
        idProduk = input("ID Produk: ").strip() #menghapus spasi didepan maupun belakang
        if not idProduk: #agar input tidak bisa kosong
            raise ValueError(Fore.RED + "input tidak boleh kosong" + Style.RESET_ALL) 
        if not idProduk.isdigit(): #agar input hanya bisa angka
            raise ValueError(Fore.RED + "Input harus berupa Angka" + Style.RESET_ALL)
        if idProduk in produkDF['id'].astype(str).values: #melakukan pengecekkan apakah id sudah ada di data sebelumnya
            raise ValueError (Fore.RED + 'ID sudah tersedia di data' + Style.RESET_ALL)
        nama = input("Nama Produk: ").strip() 
        if not nama:
            raise ValueError(Fore.RED + 'input tidak boleh kosong' + Style.RESET_ALL)
        hargaBaru = input("Harga: ").strip() #dibuat string terlebih dahulu agar lebih mudah pada error handling
        if not hargaBaru:
            raise ValueError(Fore.RED + "input tidak boleh kosong" + Style.RESET_ALL)
        if not hargaBaru.isnumeric():
            raise ValueError(Fore.RED + "Harga harus berupa Angka" + Style.RESET_ALL)
        harga = float(hargaBaru) #mengubah jenis data menjadi float
        stokBaru = input("Stok: ").strip() 
        if not stokBaru:
            raise ValueError (Fore.RED + 'Input tidak boleh kosong' + Style.RESET_ALL)
        if not stokBaru.isdigit():
            raise ValueError (Fore.RED + 'Input harus berupa Angka' + Style.RESET_ALL)
        stok = int(stokBaru) #mengubah data stok menjadi int agar tidak menjadi bilangan pecahan
        produkBaru = pd.DataFrame({'id': [idProduk], 'nama': [nama], 'harga': [harga], 'stok': [stok]}) #menggunakan nilai nilai sebelumnya ke DF
        produkDF = pd.concat([produkDF, produkBaru], ignore_index=True) #menggabungkan data
        produkDF.to_csv('produk.csv', index=False) #melakukan push ke csv
        input(Fore.GREEN + "Produk berhasil ditambahkan! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
    except ValueError as e:
        print(e)
    input("Tekan enter untuk melanjutkan....")


def editPr():
    while True:
        print("\n=== UBAH PRODUK ===")
        idInput = input("Masukkan id produk yang akan diubah: ").strip()
        if idInput.isalpha():
            print(Fore.RED + "Input harus berupa Angka" + Style.RESET_ALL)
            input("Tekan Enter untuk melanjutkan")
            return

        if idInput:
            try:
                idProduk = int(idInput)
                produkDF = pd.read_csv('produk.csv')
                
                if idProduk in produkDF['id'].values:
                    
                    Produk = produkDF.loc[produkDF['id'] == idProduk].iloc[0] #mencari id produk sesuai dengan input yang dilakukan
                    
                    
                    nama = input("Nama Produk baru: ").strip()
                    harga = input("Harga baru: ").strip()
                    if harga.isalpha():
                        raise ValueError ('Input harus berupa Angka')
                    stok = input("Stok baru: ").strip()
                    if stok.isalpha():
                        raise ValueError ('Input harus berupa Angka')
                    
                    
                    namaBaru = nama if nama else Produk['nama'] #menggunakan nilai lama jika input kosong
                    hargaBaru = float(harga) if harga.isdigit() else Produk['harga'] #menggunakan nilai lama jika input kosong, atauu selain angka
                    stokBaru = int(stok) if stok.isdigit() else Produk['stok'] #menggunakan nilai lama jika input kosong, atau selain angka
                    
                    
                    produkDF.loc[produkDF['id'] == idProduk, ['nama', 'harga', 'stok']] = [namaBaru, hargaBaru, stokBaru] #mengubah nilai data lama menjadi data baru
                    produkDF.to_csv('produk.csv', index=False) #push ke csv
                    
                    input(Fore.GREEN + "Produk berhasil diubah! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
                    break
                else:
                    input(Fore.RED + "Produk tidak ditemukan! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
                    break
            except ValueError as e:
                print(Fore.RED + f"Terjadi Kesalahan {e}" + Style.RESET_ALL)
                input("Tekan Enter untuk melanjutkan")
                return
        else:
            print(Fore.RED + "Input tidak boleh kosong." + Style.RESET_ALL)
            input("Tekan Enter untuk mencoba lagi...")
            return

def hapusPr():
    try:
        print("\n=== HAPUS PRODUK ===")
        idProdukBaru = input("Masukkan ID produk yang akan dihapus: ").strip()
        if not idProdukBaru:
            raise ValueError (Fore.RED + 'Input tidak boleh kosong ' + Style.RESET_ALL) #error handling jika melakukan input kosong
        if idProdukBaru.isalpha():
            raise ValueError (Fore.RED + 'Input harus berupa angka' + Style.RESET_ALL)
        
        idProduk = int(idProdukBaru)
        produkDF = pd.read_csv('produk.csv')
        if idProduk in produkDF['id'].values: 
            produkDF = produkDF[produkDF['id'] != idProduk] #membuat DF baru dimana hanya id yang tidak sama yg disimpan
            produkDF.to_csv('produk.csv', index=False)
            input("Produk berhasil dihapus! Tekan Enter untuk melanjutkan...")
        else:
            input(Fore.RED + "Produk tidak ditemukan! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
    except ValueError as e:
        print(Fore.RED + f"Terjadi Kesalahan {e}" + Style.RESET_ALL)
        input("Tekan Enter untuk melanjutkan")

def performaSales():
    clear()
    while True:
        clear()
        salesDF = pd.read_csv('sales.csv')
        if salesDF.empty:
            print(Fore.RED + "Tidak ada data!" + Style.RESET_ALL)
        else:
            print("\nPerforma Sales:")
            tabelSales = PrettyTable()
            tabelSales.field_names = ["Nama", "Target", "Bonus"]

            for _, row in salesDF.iterrows():
                rupiahSales = f"Rp {row['target']:,.2f}" #membuat format rupiah
                bonusSales = f"Rp {row['bonus']:,.2f}" #membuat format rupiah
                tabelSales.add_row([row['username'], rupiahSales, bonusSales])
            print(tabelSales)
        
        
        print("\n=== MENU PERFORMA SALES ===")
        print("1. Hapus Sales")
        print("2. Ubah Target dan Bonus Sales")
        print("0. Kembali")
        
        choice = input("Pilih menu: ")
        
        if choice == "1":
            hapusSales()
        elif choice == "2":
            editTarget()
        elif choice == "0":
            break
        else:
            input(Fore.RED + "Menu tidak valid! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)

def hapusSales():
    username = input("Masukkan username sales yang akan dihapus: ")
    
    salesDF = pd.read_csv('sales.csv')
    userDF = pd.read_csv('user.csv')
    
    if username in salesDF['username'].values:
        salesDF = salesDF[salesDF['username'] != username] #hanya menyimpan data yang tidak sama dengan input
        userDF = userDF[userDF['username'] != username] #hanya menyimpan data yang tidak sama dengan input 
        
        salesDF.to_csv('sales.csv', index=False)
        userDF.to_csv('user.csv', index=False)
        input(Fore.RED + "Sales berhasil dihapus! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)
    else:
        input(Fore.RED + "Sales tidak ditemukan! Tekan Enter untuk melanjutkan..." + Style.RESET_ALL)

def editTarget():
    try:
        username = input("Masukkan username sales: ")
        if not username:
            raise ValueError (Fore.RED + "Username tidak boleh kosong!" + Style.RESET_ALL)
        if not re.match("^[A-Za-z0-9]*$", username): #username hanya boleh berisi karakter a-z, A-Z, 0-9
            raise ValueError(Fore.RED + "Username hanya boleh mengandung huruf dan angka tanpa karakter spesial!" + Style.RESET_ALL)
    
        
        salesDF = pd.read_csv('sales.csv')
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk kembali")
    try:
        salesDF = pd.read_csv('sales.csv')
        if username in salesDF['username'].values:
            targetBaru = input("Target baru: ") #menggunakan data str agar lebih mudah pada saat error handling
            if not targetBaru:
                raise ValueError (Fore.RED + 'Input tidak boleh kosong' + Style.RESET_ALL)
            if not targetBaru.isnumeric(): #jika input bukan angka maka akan terjadi error
                raise ValueError (Fore.RED + 'Input harus berupa Angka' + Style.RESET_ALL)
        
            target = float(targetBaru) #mengubah jenis data
            if target < 0:
                raise ValueError (Fore.RED + 'Target tidak boleh kurang dari 0' + Style)
            
            bonusBaru = input("Bonus baru: ")
            if not bonusBaru:
                raise ValueError (Fore.RED + 'Input tidak boleh kosong' + Style.RESET_ALL)
            if not bonusBaru.isnumeric():
                raise ValueError (Fore.RED + 'Input harus berupa angka' + Style.RESET_ALL)
            bonus = float(bonusBaru)
            if bonus < 0:
                raise ValueError (Fore.RED + 'Bonus tidak boleh kurang dari 0' + Style)
            
            salesDF.loc[salesDF['username'] == username, ['target', 'bonus']] = [target, bonus]
            salesDF.to_csv('sales.csv', index=False)
            input("Target dan bonus berhasil diubah! Tekan Enter untuk melanjutkan...")
        else:
            input(Fore.RED + "Sales tidak ditemukan\n Tekan enter untuk melanjutkan" + Style.RESET_ALL)
            return
    except ValueError as e:
        print(Fore.RED + "Terjadi kesalahan {e}" + Style.RESET_ALL)
        input("Tekan Enter untuk melanjutkan")

def dataSales():
    clear()
    transaksiDF = pd.read_csv('history.csv')
    if transaksiDF.empty:
        print("Belum ada penjualan.")
    else:
        tabelPenjualan = PrettyTable()
        tabelPenjualan.field_names = ["Tanggal", "Id Produk", "Jumlah", "Total", "Nama"]
        for _, row in transaksiDF.iterrows():
            rupiah = f"Rp {row['total']:,.2f}" #mengubah format menjadi rupiah
            idProduk = int(row['id_produk']) #mengubah format menjadi int
            tabelPenjualan.add_row([row['tanggal'], idProduk, row['jumlah'], rupiah, row['nama_sales']])
        print(tabelPenjualan)
    input("\nTekan Enter untuk melanjutkan...")

def dataKeuangan():
    clear()
    transaksiDF = pd.read_csv('history.csv')
    if transaksiDF.empty:
        print("Belum ada data keuangan.")
    else:
        total_income = transaksiDF['total'].sum() #menjumlahkan total pendapatan
        print(f"\nTotal Pendapatan: Rp {total_income:,.2f}") 
    input("\nTekan Enter untuk melanjutkan...")

def visualisasi():
    
    transaksiDF = pd.read_csv('history.csv')
    
    
    if transaksiDF.empty:
        print("Belum ada data untuk divisualisasikan.")
        input("Tekan Enter Untuk Melanjutkan")
        return
    
    transaksiDF['tanggal'] = pd.to_datetime(transaksiDF['tanggal'], dayfirst=True) #mengubah menjadi dd/mm/yy
    
    penjualanBulanan = transaksiDF.groupby(transaksiDF['tanggal'].dt.to_period('M'))['total'].sum() #mengelompokkan data berdasarkan bulan dan menjumlahkan total setiap bulan
    
    plt.figure(figsize=(15, 6)) #membuat gambar dengan ukuran 15x6
    penjualanBulanan.plot(kind='line', marker='o') #menambah titik pada setiap data point
    plt.title('Total Penjualan per Bulan (Rp)') #judul
    plt.xlabel('Bulan') #sumbu x
    plt.ylabel('Total Penjualan (Rp)') #sumbu y
    plt.xticks(rotation=90)  #memutar 90 derajat agar lebih mudah diliat
    
    
    plt.ticklabel_format(style='plain', axis='y') #menampilkan angka dalam format normal
    
    plt.tight_layout() #mengatur spacing secara otomatis
    plt.show(block=True) #membuat program akan menunggu sampai grafik di tutup oleh pengguna

def midPrint(text, width=50):
    spaces = (width - len(text)) // 2 #menghitung jumlah spasi yang dibutuhkan di setiap sisi
    extra_space = (width - len(text)) % 2  #Menghitung spasi jika panjangnya ganjil
    return " " * spaces + text + " " * (spaces + extra_space) #mengembalikkan dan menambahkan 

def adminMenu(username):
    clear()
    width = 50  # Lebar bingkai
    while True:
        clear()
        # Membuat tampilan header
        print(Fore.CYAN + Style.BRIGHT + "=" * width)
        print(midPrint(f"Selamat datang, {username}!", width))
        print("=" * width + Style.RESET_ALL)

        # Menampilkan menu di tengah bingkai
        print("|" + " " * (width - 2) + "|")
        print("|" + midPrint("=== MENU ADMIN ===", width - 2) + "|")
        print("|" + " " * (width - 2) + "|")
        print("|" + midPrint("1. Lihat Produk", width - 2) + "|")
        print("|" + midPrint("2. Status Performa Sales", width - 2) + "|")
        print("|" + midPrint("3. Lihat Penjualan", width - 2) + "|")
        print("|" + midPrint("4. Lihat Keuangan", width - 2) + "|")
        print("|" + midPrint("5. Visualisasi Data", width - 2) + "|")
        print("|" + midPrint("0. Logout", width - 2) + "|")
        print("|" + " " * (width - 2) + "|")
        print("=" * width)

        # Input pilihan
        choice = input(Fore.YELLOW + Style.BRIGHT + "Pilih menu: " + Style.RESET_ALL)
        
        # Menu navigasi
        if choice == "1":
            menuProduk()
        elif choice == "2":
            performaSales()
        elif choice == "3":
            dataSales()
        elif choice == "4":
            dataKeuangan()
        elif choice == "5":
            visualisasi()
        elif choice == "0":
            break
        else:
            input("Menu tidak valid! Tekan Enter untuk melanjutkan...")
