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
            df = pd.DataFrame.from_dict(produk, orient='index', columns=['nama', 'harga', 'stok'])
            df.index.name = 'No'
            df.reset_index(inplace=True)
            print(f"\n{'No':<5} {'Nama':<17} {'Harga (IDR)':<15} {'Stok':<4}")
            print("=" * 65)
            for _, row in df.iterrows():
                print(f"{row['No']:<5} {row['nama']:<17} {row['harga']:<15,} {row['stok']:<4}")
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
            print("=" * 7, f"Hi {username} Apa yang ingin anda lakukan?", "=" * 7,"\n1. Lihat Produk\n2. Beli Produk\n3. History Pembelian\n4. Total Belanja\n0. Back")
            
            pilih = input("Pilih menu : ")
            
            if pilih == "1":
                showPr()
                input("Tekan Enter untuk melanjutkan...")
            elif pilih == "2":
                buy(username)
            elif pilih == "3":
                riwayatUser(username)
            elif pilih == "4":
                lihatTotalBelanja(username)
            elif pilih == "0":
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk melanjutkan...")
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")
            input("Tekan Enter untuk melanjutkan...")

def addPr():
    try:
        clear()
        print("=" * 9, "TAMBAH PRODUK", "=" * 9)
        nama = input("Nama produk: ")
        harga = int(input("Harga produk: "))
        stok = int(input("Stok produk: "))
        
        No = max(produk.keys()) + 1 if produk else 1
        produk[No] = {"nama": nama, "harga": harga, "stok": stok}
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
        
        if No in produk:
            nama = input("Nama baru (kosongkan jika tidak ingin diubah): ")
            if nama:
                produk[No]["nama"] = nama
            
            harga = input("Harga baru (kosongkan jika tidak ingin diubah): ")
            if harga:
                produk[No]["harga"] = int(harga)
            
            stok = input("Stok baru (kosongkan jika tidak ingin diubah): ")
            if stok:
                produk[No]["stok"] = int(stok)
            
            print("Produk berhasil diupdate!")
        else:
            print("Produk tidak ditemukan!")
        input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("No produk, harga, dan stok harus berupa angka!")
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")

def delPr():
    try:
        showPr()
        No = int(input("Masukkan No produk yang ingin dihapus: "))
        
        if No in produk:
            del produk[No]
            print("Produk berhasil dihapus!")
        else:
            print("Produk tidak ditemukan!")
        input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("No produk harus berupa angka!")
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")

def buy(username):
    try:
        showPr()
        No = int(input("Masukkan No produk yang akan dibeli: "))
        jumlah = int(input("Masukkan jumlah yang akan dibeli: "))
        
        if No in produk:
            if produk[No]["stok"] >= jumlah:
                total = produk[No]["harga"] * jumlah
                confirmation = input(f"Total pembayaran: Rp{total:,}. Apakah anda yakin? (y/n): ")
                if confirmation.lower() == 'y':
                    id_transaksi = len(listTerjual) + 1
                    listTerjual.append({
                        "id": id_transaksi,
                        "username": username,
                        "produk_id": No,
                        "jumlah": jumlah,
                        "total": total
                    })
                    produk[No]["stok"] -= jumlah
                    print(f"Pembelian berhasil!\nTotal: Rp{total:,}\nDitunggu Repeat ordernya!")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("Stok tidak mencukupi!")
                input("Tekan Enter untuk melanjutkan...")
        else:
            print("Produk tidak ditemukan!")
            input("Tekan Enter untuk melanjutkan...")
    except ValueError:
        print("No produk dan jumlah harus berupa angka!")
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")

def terjual():
    clear()
    print("=" * 9 ,"DAFTAR PENJUALAN", "=" * 9)
    try:
        if listTerjual:
            df = pd.DataFrame(listTerjual)
            df['Produk'] = df['produk_id'].map(lambda x: produk.get(x, {}).get('nama', 'Produk Dihapus'))
            print(df[['id', 'username', 'Produk', 'jumlah', 'total']].to_string(index=False, formatters={'total': lambda x: f"{x:,}"}))
        else:
            print("Belum ada Transaksi")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
    input("\nTekan Enter untuk melanjutkan...")

def riwayatUser(username):
    clear()
    print(f"=" * 7, f"RIWAYAT PEMBELIAN {username}", "=" * 7)
    
    try:
        userlistTerjual = [sale for sale in listTerjual if sale['username'] == username]
        
        if userlistTerjual:
            print(f"{'ID':<5} {'Produk':<20} {'Jumlah':<10} {'Total (IDR)':<15}")
            print("=" * 50)
            
            for sale in userlistTerjual:
                namaProduk = produk.get(sale['produk_id'], {}).get('nama', 'Produk Dihapus')
                print(f"{sale['id']:<5} {namaProduk:<20} {sale['jumlah']:<10} {sale['total']:<15,}")
        else:
            print("Belum ada pembelian.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
    input("\nTekan Enter untuk melanjutkan...")

def totalBelanja(index, username):
    if index >= len(listTerjual):
        return 0
    transaksi = listTerjual[index]
    totalR = totalBelanja(index + 1, username)
    
    if transaksi['username'] == username: #menambahkan jika username sesuai
        return transaksi['total'] + totalR
    
    return totalR

def lihatTotalBelanja(username):
    clear()
    print(f"=" * 7, f"TOTAL BELANJA {username}", "=" * 7)
    total = totalBelanja(0, username)
    print(f"\nTotal belanja Anda: Rp{total:,}")
    input("\nTekan Enter untuk melanjutkan...")