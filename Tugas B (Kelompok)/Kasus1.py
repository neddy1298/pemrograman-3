print("\n Hallo Selamat Datang di Kalkulator Geometri")
print("\n =============================================")

print("\n Pilih Bentuk Geometri:")
print("1) Bola")
print("2) Kubus")
print("3) Balok")

pilihan = int(input("Masukkan Pilihan Geometri (1/2/3) : "))

print("\n Selanjutnya, pilih operasi yang akan dihitung;")
print("1. Keliling") 
print("2. Luas")
print("3. Volume")

pilihan2 = int(input("Operasi yang dipilih (1/2/3) : "))


if pilihan == 1:
    r = int(input("Masukkan jari-jari: "))
    if pilihan2 == 1:
        print("Keliling bola adalah", 2 * 3.14 * r)
    elif pilihan2 == 2:
        print("Luas bola adalah", 4 * 3.14 * r ** 2)
    elif pilihan2 == 3:
        print("Volume bola adalah", 4 / 3 * 3.14 * r ** 3)
    else:
        print("Pilihan tidak valid")

elif pilihan == 2:
    s = int(input("Masukkan sisi: "))

    if pilihan2 == 1:
        print("Keliling kubus adalah", 12 * s)
    elif pilihan2 == 2:
        print("Luas kubus adalah", 6 * s ** 2)
    elif pilihan2 == 3:
        print("Volume kubus adalah", s ** 3)
    else:
        print("Pilihan tidak valid")
elif pilihan == 3:
    p = int(input("Masukkan panjang: "))
    l = int(input("Masukkan lebar: "))
    t = int(input("Masukkan tinggi: "))

    if pilihan2 == 1:
        print("Keliling balok adalah", 4 * (p + l + t))
    elif pilihan2 == 2:
        print("Luas balok adalah", 2 * (p * l + p * t + l * t))
    elif pilihan2 == 3:
        print("Volume balok adalah", p * l * t)
    else:
        print("Pilihan tidak valid")
else:
    print("Pilihan tidak valid")