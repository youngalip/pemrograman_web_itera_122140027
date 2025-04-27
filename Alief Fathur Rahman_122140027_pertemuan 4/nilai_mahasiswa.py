class Mahasiswa:
    def __init__(self, nama, nim, nilai_uts, nilai_uas, nilai_tugas):
        self.nama = nama
        self.nim = nim
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
        self.nilai_tugas = nilai_tugas
        self.nilai_akhir = 0
        self.grade = ''

    def hitung_nilai_akhir(self):
        self.nilai_akhir = (self.nilai_uts * 0.3) + (self.nilai_uas * 0.4) + (self.nilai_tugas * 0.3)

    def tentukan_grade(self):
        if self.nilai_akhir >= 80:
            self.grade = 'A'
        elif self.nilai_akhir >= 70:
            self.grade = 'B'
        elif self.nilai_akhir >= 60:
            self.grade = 'C'
        elif self.nilai_akhir >= 50:
            self.grade = 'D'
        else:
            self.grade = 'E'

    def tampilkan_data(self):
        return f"{self.nama:<15} {self.nim:<10} {self.nilai_akhir:<10.2f} {self.grade:<5}"

class PengelolaNilai:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa_list.append(mahasiswa)

    def tampilkan_semua_mahasiswa(self):
        print(f"{'Nama':<15} {'NIM':<10} {'Nilai Akhir':<10} {'Grade':<5}")
        for mhs in self.mahasiswa_list:
            print(mhs.tampilkan_data())

    def nilai_tertinggi_terendah(self):
        tertinggi = max(self.mahasiswa_list, key=lambda mhs: mhs.nilai_akhir)
        terendah = min(self.mahasiswa_list, key=lambda mhs: mhs.nilai_akhir)
        print(f"\nMahasiswa dengan nilai tertinggi: {tertinggi.nama} ({tertinggi.nilai_akhir:.2f})")
        print(f"Mahasiswa dengan nilai terendah: {terendah.nama} ({terendah.nilai_akhir:.2f})")

if __name__ == "__main__":
    pengelola = PengelolaNilai()

    mahasiswa1 = Mahasiswa("Budi", "122140001", 85, 90, 80)
    mahasiswa2 = Mahasiswa("Ani", "122140002", 70, 75, 65)
    mahasiswa3 = Mahasiswa("Citra", "122140003", 60, 55, 70)
    mahasiswa4 = Mahasiswa("Dodi", "122140004", 90, 85, 95)
    mahasiswa5 = Mahasiswa("Eka", "122140005", 50, 60, 55)

    for mhs in [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4, mahasiswa5]:
        mhs.hitung_nilai_akhir()
        mhs.tentukan_grade()

    pengelola.tambah_mahasiswa(mahasiswa1)
    pengelola.tambah_mahasiswa(mahasiswa2)
    pengelola.tambah_mahasiswa(mahasiswa3)
    pengelola.tambah_mahasiswa(mahasiswa4)
    pengelola.tambah_mahasiswa(mahasiswa5)

    pengelola.tampilkan_semua_mahasiswa()

    pengelola.nilai_tertinggi_terendah()
