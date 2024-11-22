import os
import pandas as pd
from colorama import Fore, Style, init
from prettytable import PrettyTable
from datetime import datetime
from admin import midPrint, clear

def produk():
    clear()
    produkDF = pd.read_csv('produk.csv')
    if produkDF.empty:
        print("Belum ada produk.")
    else:
        table = PrettyTable()
        table.field_names = ["no", "Nama produk", "Price", "Stock"]
        
        for _, row in produkDF.iterrows():
            rupiah = f"Rp {row['harga']:,.2f}"
            table.add_row([row['id'], row['nama'], rupiah, row['stok']])
        
        print(table)
    input("Tekan enter untuk melanjutkan ...")


def dataSales(username):
    clear()
    transaksiDF = pd.read_csv('history.csv') #membaca file csv
    transaksiUser = transaksiDF[transaksiDF['nama_sales'] == username] #melakukan pengecekkan username yang login
    if transaksiUser.empty:
        print("Anda belum memiliki penjualan.")
    else:
        showSales = PrettyTable()
        showSales.field_names = ["Tanggal", "Id Produk", "Jumlah", "Harga", "Nama"]
        
        for _, row in transaksiDF.iterrows(): #membaca file perbaris
            rupiah = f"Rp {row['total']:,.2f}"
            showSales.add_row([row['tanggal'], row['id_produk'], row['jumlah'], rupiah, row["nama_sales"]])
        print(showSales)

    input("\nTekan Enter untuk melanjutkan...")

def performa(username):
    clear()
    salesDF = pd.read_csv('sales.csv') #membaca file csv ke df
    transaksiDF = pd.read_csv('history.csv') #membaca file csv ke df
    
    if username not in salesDF['username'].values:
        print("Anda belum memiliki penjualan.")
        input ('tekan enter untuk melanjutkan')
        return
    
    sales = salesDF[salesDF['username'] == username]
    target = sales['target'].values[0]
    bonus = sales['bonus'].values[0]
    
    totalSales = transaksiDF[transaksiDF['nama_sales'] == username]['total'].sum() #melakukan penjumlahan
    
    print(f"\nPerforma Anda:")
    print(f"Target: Rp {target:,.2f}")
    print(f"Total Penjualan: Rp {totalSales:,.2f}")
    print(f"Progress: {(totalSales/target)*100:.2f}%")
    if totalSales >= target:
        print(f"Selamat! Anda mencapai target dan mendapatkan bonus Rp {bonus:,.2f}")
    else:
        sisa = target - totalSales
        print(f"Sisa target yang harus dicapai: Rp {sisa:,.2f}")
    input("\nTekan Enter untuk melanjutkan...")

def produkTerjual(username):
    clear()
    print("\n=== JUAL PRODUK ===")
    produk_df = pd.read_csv('produk.csv')
    
    if produk_df.empty:
        input("Tidak ada produk yang tersedia. Tekan Enter untuk melanjutkan...")
        return
        
    print("\nDaftar Produk yang Tersedia:")
    tabelJual = PrettyTable()
    tabelJual.field_names = ["Id ", "Nama Produk", "Harga", "Stok"]
    for _, row in produk_df.iterrows():
        rupiahHarga = f"Rp {row['harga']:,.2f}"
        tabelJual.add_row([row['id'],row['nama'],rupiahHarga,row['stok']])
    print(tabelJual)
    try:
        id_produkBaru = input("\nMasukkan ID produk yang akan dijual: ").strip() #menghapus spasi didepan maupun dibelakang
        if not id_produkBaru:
            raise ValueError(Fore.RED + "Input tidak boleh kosong" + Style.RESET_ALL)
        if id_produkBaru.isalpha():
            raise ValueError (Fore.RED + "Input harus berupa angka" + Style.RESET_ALL)
        
        
    except ValueError as e:
        print(e)
    try:
        id_produk = int(id_produkBaru)
        produk_df = pd.read_csv('produk.csv')
        if int(id_produk) in produk_df['id'].values:
            product = produk_df[produk_df['id'] == int(id_produk)]
            jumlah = int(input("Jumlah yang akan dijual: "))
            if jumlah < 1:
                raise ValueError(Fore.RED + "Jumlah harus lebih dari 0" + Style.RESET_ALL)
            if not jumlah:
                raise ValueError("Input tidak boleh kosong")
            if jumlah <= 0:
                print("Stok telah habis")
            
            if jumlah <= product['stok'].iloc[0]:
                total = jumlah * product['harga'].iloc[0] #iloc berfungsi untuk membaca int sesuai namanya (integer location)
                tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #format tanggal
                
                produk_df.loc[produk_df['id'] == int(id_produk), 'stok'] -= jumlah #melakukan pengurangan stok
                produk_df.to_csv('produk.csv', index=False)
                
                transaksiDF = pd.read_csv('history.csv')
                transaksiBaru = pd.DataFrame({
                    'tanggal': [tanggal],
                    'id_produk': [id_produk],
                    'jumlah': [jumlah],
                    'total': [total],
                    'nama_sales': [username]
                })
                transaksiDF = pd.concat([transaksiDF, transaksiBaru], ignore_index=True) #menggabungkan data baru
                transaksiDF.to_csv('history.csv', index=False)
                
                print(f"\nPenjualan berhasil!")
                print(f"Total: Rp {total:,.2f}")
                input("Tekan Enter untuk melanjutkan...")
            else:
                input("Stok tidak mencukupi! Tekan Enter untuk melanjutkan...")
        else:
            input("Produk tidak ditemukan! Tekan Enter untuk melanjutkan...")
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk melanjutkan")

def salesMenu(username):
    width = 50  #lebar untuk print pada terminal
    while True:
        clear()
        #header
        print(Fore.CYAN + Style.BRIGHT + "=" * width)
        print(midPrint(f"Selamat datang, {username}!", width))
        print("=" * width + Style.RESET_ALL)

        print("|" + " " * (width - 2) + "|")
        print("|" + midPrint("=== MENU SALES ===", width - 2) + "|")
        print("|" + " " * (width - 2) + "|")
        print("|" + midPrint("1. Lihat Produk", width - 2) + "|")
        print("|" + midPrint("2. Lihat Penjualan", width - 2) + "|")
        print("|" + midPrint("3. Lihat Performa", width - 2) + "|")
        print("|" + midPrint("4. Jual Produk", width - 2) + "|")
        print("|" + midPrint("0. Logout", width - 2) + "|")
        print("|" + " " * (width - 2) + "|")
        print("=" * width)

        choice = input(Fore.YELLOW + Style.BRIGHT + "Pilih menu: " + Style.RESET_ALL)
        
        if choice == "1":
            produk()
        elif choice == "2":
            dataSales(username)
        elif choice == "3":
            performa(username)
        elif choice == "4":
            produkTerjual(username)
        elif choice == "0":
            break
        else:
            input("Menu tidak valid! Tekan Enter untuk melanjutkan...")
