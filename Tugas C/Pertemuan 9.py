import csv
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# data awal
list_data = []

def show_menu ():
    clear_screen()
    print("=== APLIKASI KONTAK ===")
    print("[1] Lihat Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[0] Exit")
    print(10 * "-")
    menu = input("Pilih menu : ")

    if menu == '1':
        menu1()
    elif menu == '2':
        menu2()
    elif menu == '3':
        menu3()
    elif menu == '4':
        menu4()
    elif menu == '0':
        print("Terimakasih Telah Berkunjung")
        exit()
    else:
        print("Menu yang anda masukan tidak ada, Masukan Pilihan yang tersedia...!")
        kembali()
        
def menu1():
    print('Nim || Nama')
    index = 0
    if len(list_data) <= 0:
        print("Data Kosong")
    else:
        for data in list_data:
            print(data[0],data[1])
    
    kembali()
    
def menu2():
    nim = input("Masukan Nim: ")
    nama = input("Masukan Nama: ")
    list_data.append([nim,nama])
    print("Data berhasil di tambahkan")
    kembali()

def menu3():
    nim = input("Masukan Nim: ")

    index = cari_data(nim)

    nama = input("Masukan Nama Baru: ")
    list_data[index] = [nim,nama]
    print('Data Anda telah dirubah')
    kembali()

def menu4():
    nim = input("Masukan Nim: ")

    index = cari_data(nim)
    
    del list_data[index]
    print("Data berhasil di hapus")
    kembali()

def cari_data(nim):
    index = 0
    for data in list_data:
        if data[0] == nim:
            return index
        index += 1
    
    print("Data tidak ditemukan")
    kembali()
    

def kembali():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

while(True):
    show_menu()