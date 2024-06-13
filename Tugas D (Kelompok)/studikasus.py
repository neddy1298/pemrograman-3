import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()
cursor.execute("""
    CREATE DATABASE IF NOT EXISTS db_studi_kasus;
""")
cursor.execute("""
    USE db_pertemuan11_studi_kasus
""")
cursor.execute("""
        CREATE TABLE IF NOT EXISTS mahasiswa (
            nim VARCHAR(255),
            nama VARCHAR(255),
            kelas VARCHAR(255)
        )
    """)


def menu():
    print("""
=== Aplikasi Database Python ===
[1] Tambah data
[2] Ubah data
[3] Hapus data
[4] Tampilkan data
[5] Cari Data
[0] Keluar
""")
    pilihan = int(input("Pilih menu> "))
    if pilihan == 1:
        tambah_data()
    elif pilihan == 2:
        ubah_data()
    elif pilihan == 3:
        hapus_data()
    elif pilihan == 4:
        tampilkan_data()
    elif pilihan == 5:
        cari_data()
    else:
        exit()


def tambah_data():
    print("Masukkan data mahasiswa")
    nim = input("NIM: ")
    nama = input("Nama: ")
    kelas = input("Kelas: ")

    sql = "INSERT INTO mahasiswa(nim, nama, kelas) VALUES (%s, %s, %s)"
    val = (nim, nama, kelas)
    cursor.execute(sql, val)

    db.commit()

    print("{} data berhasil disimpan".format(cursor.rowcount))
    input("Tekan ENTER untuk kembali ke menu")
    menu()


def ubah_data():
    print("Masukkan data mahasiswa yang akan diubah")
    nim = input("NIM: ")
    nama = input("Nama: ")
    kelas = input("Kelas: ")

    sql = "UPDATE mahasiswa SET nama=%s, kelas=%s WHERE nim=%s"
    val = (nama, kelas, nim)
    cursor.execute(sql, val)

    db.commit()

    print("{} data berhasil diubah".format(cursor.rowcount))
    input("Tekan ENTER untuk kembali ke menu")
    menu()


def hapus_data():
    print("Masukkan NIM mahasiswa yang akan dihapus")
    nim = input("NIM: ")

    sql = "DELETE FROM mahasiswa WHERE nim=%s"
    val = (nim,)
    cursor.execute(sql, val)

    db.commit()

    print("{} data berhasil dihapus".format(cursor.rowcount))
    input("Tekan ENTER untuk kembali ke menu")
    menu()


def tampilkan_data():
    sql = "SELECT * FROM mahasiswa"
    cursor.execute(sql)

    results = cursor.fetchall()

    for data in results:
        print(data)
    input("Tekan ENTER untuk kembali ke menu")
    menu()


def cari_data():
    print("Masukkan NIM / Kelas / Nama mahasiswa yang akan dicari")
    cari = input("Cari: ")
    cari = "%" + cari + "%"

    sql = "SELECT * FROM mahasiswa WHERE nim LIKE %s OR nama LIKE %s OR kelas LIKE %s"
    val = (cari, cari, cari)
    cursor.execute(sql, val)

    results = cursor.fetchall()

    if cursor.rowcount <= 0:
        print("Data tidak ditemukan")
    else:
        for data in results:
            print(data)
    input("Tekan ENTER untuk kembali ke menu")
    menu()


menu()
