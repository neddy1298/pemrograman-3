# Tugas 1-b

berat_badan = int(input("Berat badan (kg) = "))
tinggi_badan = int(input("Tinggi badan (cm) = "))

# Convert tinggi badan dari cm ke m
tinggi_badan = (tinggi_badan / 100) ** 2

IMT = berat_badan / tinggi_badan


if IMT < 18.5:
    print("IMT = " + IMT)
    print("Status Gizi = Underweight")
elif IMT < 24.9:
    print("IMT = " + IMT)
    print("Status Gizi = Normal Range")
elif IMT < 29.9:
    print("IMT = " + IMT)
    print("Status Gizi = Overweight")
elif IMT < 34.9:
    print("IMT = " + IMT)
    print("Status Gizi = Obese Class 1")
elif IMT < 39.9:
    print("IMT = " + IMT)
    print("Status Gizi = Obese Class 2")
else:
    print("IMT = " + IMT)
    print("Status Gizi = Obese Class 3")
