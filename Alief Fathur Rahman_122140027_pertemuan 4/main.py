import math_operations

def tampilkan_hasil(label, hasil):
    print(f"{label:<30}: {hasil:.2f}")

print("="*50)
print(f"{'Program Penghitungan Geometri & Konversi Suhu':^50}")
print("="*50)

sisi = 5
print("\n" + "-"*50)
print(f"{'Persegi':^50}")
print("-"*50)
print(f"Sisi persegi: {sisi}")
tampilkan_hasil("Luas Persegi", math_operations.hitung_luas_persegi(sisi))
tampilkan_hasil("Keliling Persegi", math_operations.hitung_keliling_persegi(sisi))

panjang = 8
lebar = 4
print("\n" + "-"*50)
print(f"{'Persegi Panjang':^50}")
print("-"*50)
print(f"Panjang: {panjang}, Lebar: {lebar}")
tampilkan_hasil("Luas Persegi Panjang", math_operations.hitung_luas_persegi_panjang(panjang, lebar))
tampilkan_hasil("Keliling Persegi Panjang", math_operations.hitung_keliling_persegi_panjang(panjang, lebar))

radius = 7
print("\n" + "-"*50)
print(f"{'Lingkaran':^50}")
print("-"*50)
print(f"Radius: {radius}")
tampilkan_hasil("Luas Lingkaran", math_operations.hitung_luas_lingkaran(radius))
tampilkan_hasil("Keliling Lingkaran", math_operations.hitung_keliling_lingkaran(radius))

celsius = 25
print("\n" + "-"*50)
print(f"{'Konversi Suhu':^50}")
print("-"*50)
print(f"Suhu dalam Celsius: {celsius}°C")
tampilkan_hasil("Celsius ke Fahrenheit", math_operations.celsius_ke_fahrenheit(celsius))
tampilkan_hasil("Celsius ke Kelvin", math_operations.celsius_ke_kelvin(celsius))

print("="*50)
