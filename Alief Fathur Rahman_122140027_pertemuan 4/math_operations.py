PI = 3.14159

def hitung_luas_persegi(sisi):
    """Menghitung luas persegi"""
    return sisi ** 2

def hitung_keliling_persegi(sisi):
    """Menghitung keliling persegi"""
    return 4 * sisi

def hitung_luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang"""
    return panjang * lebar

def hitung_keliling_persegi_panjang(panjang, lebar):
    """Menghitung keliling persegi panjang"""
    return 2 * (panjang + lebar)

def hitung_luas_lingkaran(radius):
    """Menghitung luas lingkaran"""
    return PI * radius ** 2

def hitung_keliling_lingkaran(radius):
    """Menghitung keliling lingkaran"""
    return 2 * PI * radius

def celsius_ke_fahrenheit(celsius):
    """Mengkonversi suhu dari Celsius ke Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_ke_kelvin(celsius):
    """Mengkonversi suhu dari Celsius ke Kelvin"""
    return celsius + 273.15
