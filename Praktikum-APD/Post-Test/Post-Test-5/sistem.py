import pandas as pd
import time
from data import produk, listTerjual
from login import clear

def load(panjangLoading=30, waktu=3.5):
    for i in range(panjangLoading + 1):
        time.sleep(waktu / panjangLoading)  
        bar = "=" * i + "-" * (panjangLoading - i)  
        print(f"\rLoading: [{bar}] {i * 100 // panjangLoading}%", end="")

def showPr():
    clear()  
    print("-" * 25, "DAFTAR PRODUK", "-" * 25)
    
    try:
        if produk:
            df = pd.DataFrame(produk, columns=['No', 'Nama', 'Harga', 'Stok'])
            print(f"\n{'No':<5} {'Nama':<17} {'Harga (IDR)':<15} {'Stok':<4}")
            print("=" * 65)
            for noMor in df.values:
                print(f"{noMor[0]:<5} {noMor[1]:<17} {noMor[2]:<15,} {noMor[3]:<4}")
        else:
            print("Tidak ada produk tersedia.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan produk: {str(e)}")

def adminMenu():
    load()
    while True:
        try:
            clear()
            print("=" * 25, "MENU ADMIN", "=" * 25,"\n1. Tambah Produk\n2. Lihat Produk\n3. Update Produk\n4. Hapus Produk\n5. Lihat Penjualan\n0. Back")
            
            pilih = input("Pilih Menu : ")
            
            if pilih == "1":
                addPr()
            elif pilih == "2":
                showPr()
                input("Tekan Enter untuk melanjutkan...")
            elif pilih == "3":
                updPr()
            elif pilih == "4":
                delPr()
            elif pilih == "5":
                terjual()
            elif pilih == "0":
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk melanjutkan...")
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")
            input("Tekan Enter untuk melanjutkan...")

def userMenu(username):
    load()
    while True:
        try:
            clear()
            print("=" * 7, f"Hi {username} Apa yang ingin anda lakukan?", "=" * 7,"\n1. Lihat Produk\n2. Beli Produk\n3. History Pembelian\n0. Back")
            
            pilih = input("Pilih menu (1-4): ")
            
            if pilih == "1":
                showPr()
                input("Tekan Enter untuk melanjutkan...")
            elif pilih == "2":
                buy(username)
            elif pilih == "3":
                riwayatUser(username)
            elif pilih == "0":
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk melanjutkan...")
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")
            input("Tekan Enter untuk melanjutkan...")

#bagian crud
def addPr():
    try:
        clear()
        print("=" * 9, "TAMBAH PRODUK", "=" * 9)
        nama = input("Nama produk: ")
        harga = int(input("Harga produk: "))
        stok = int(input("Stok produk: "))
        
        No = len(produk) + 1
        produk.append([No, nama, harga, stok])
        print("Produk berhasil ditambahkan!")
        input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("Harga dan stok harus berupa angka!")
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")

def updPr():
    try:
        showPr()
        No = int(input("\nMasukkan No produk yang akan diupdate: "))
        
        for product in produk:
            if product[0] == No:
                product[1] = input("Nama baru (kosongkan jika tidak ingin diubah): ") or product[1]
                newPrice = input("Harga baru (kosongkan jika tidak ingin diubah): ")
                if newPrice:
                    product[2] = int(newPrice)
                newStock = input("Stok baru (kosongkan jika tidak ingin diubah): ")
                if newStock:
                    product[3] = int(newStock)
                print("Produk berhasil diupdate!")
                input("Tekan Enter untuk melanjutkan...")
                return
        print("Produk tidak ditemukan!")
        input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("ID produk, harga, dan stok harus berupa angka!")
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")

def delPr():
    try:
        showPr()
        No = int(input("Masukkan ID produk yang ingin dihapus: "))
        
        for product in produk:
            if product[0] == No:
                produk.remove(product)
                print("Produk berhasil dihapus!")
                input("Tekan Enter untuk melanjutkan...")
                return
        print("Produk tidak ditemukan!")
        input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("ID produk harus berupa angka!")
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")

def buy(username):
    try:
        showPr()
        No = int(input("Masukkan No produk yang akan dibeli: "))
        jumlah = int(input("Masukkan jumlah yang akan dibeli: "))
        
        for product in produk:
            if product[0] == No:
                if product[3] >= jumlah:
                    total = product[2] * jumlah
                    confirmation = input(f"Total pembayaran: Rp{total:,}. Apakah anda yakin? (y/n): ")
                    if confirmation.lower() == 'y':
                        id_transaksi = len(listTerjual) + 1
                        listTerjual.append([id_transaksi, username, No, jumlah, total])
                        product[3] -= jumlah
                        print(f"Pembelian berhasil!\nTotal: Rp{total:,}\nDitunggu Repeat ordernya!")
                    input("Tekan Enter untuk melanjutkan...")
                    return
                else:
                    print("Stok tidak mencukupi!")
                    input("Tekan Enter untuk melanjutkan...")
                    return
        print("Produk tidak ditemukan!")
        input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("ID produk dan jumlah harus berupa angka!")
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")

def terjual():
    clear()
    print("=" * 9 ,"DAFTAR PENJUALAN", "=" * 9)
    try:
        if listTerjual:
            sold = []
            for sale in listTerjual:
                namaProduk = next((p[1] for p in produk if p[0] == sale[2]), "Produk Dihapus")
                sold.append([sale[0], sale[1], namaProduk, sale[3], sale[4]])
            
            df = pd.DataFrame(sold, columns=['ID', 'Pembeli', 'Produk', 'Jumlah', 'Total'])
            print(df.to_string(index=False))
        else:
            print("Belum ada Transaksi")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
    input("\nTekan Enter untuk melanjutkan...")

def riwayatUser(username):
    clear()
    print(f"=" * 7, f"RIWAYAT PEMBELIAN {username}", "=" * 7)
    
    try:
        userlistTerjual = [sale for sale in listTerjual if sale[1] == username]
        
        if userlistTerjual:
            print(f"{'ID':<5} {'Produk':<20} {'Jumlah':<10} {'Total (IDR)':<15}")
            print("=" * 50)
            
            for sale in userlistTerjual:
                namaProduk = next((p[1] for p in produk if p[0] == sale[2]), "Produk Dihapus")
                print(f"{sale[0]:<5} {namaProduk:<20} {sale[3]:<10} {sale[4]:<15,}")
        else:
            print("Belum ada pembelian.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
    input("\nTekan Enter untuk melanjutkan...")

