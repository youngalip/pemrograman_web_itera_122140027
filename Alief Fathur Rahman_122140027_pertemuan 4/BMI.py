class BMI:
    def __init__(self, berat, tinggi):
        self.berat = berat
        self.tinggi = tinggi

    def hitung_bmi(self):
        bmi = self.berat / (self.tinggi ** 2)
        return bmi

    def kategori_bmi(self):
        bmi = self.hitung_bmi()
        if bmi < 18.5:
            return f"BMI Anda adalah {bmi:.2f}, kategori: Berat badan kurang"
        elif 18.5 <= bmi < 25:
            return f"BMI Anda adalah {bmi:.2f}, kategori: Berat badan normal"
        elif 25 <= bmi < 30:
            return f"BMI Anda adalah {bmi:.2f}, kategori: Berat badan berlebih"
        else:
            return f"BMI Anda adalah {bmi:.2f}, kategori: Obesitas"

if __name__ == "__main__":
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))

    bmi_objek = BMI(berat, tinggi)

    print(bmi_objek.kategori_bmi())
