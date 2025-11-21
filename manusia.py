
class Manusia:
    def __init__ (self, nama, jenis_kelamin, umur):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur

    def tambahUmur(self):
        self.umur = self.umur + 1

class Siswa(Manusia):
    def __init__(self, nama, jenis_kelamin, umur, kelas, nim):
        super().__init__(nama, jenis_kelamin, umur)
        self.kelas = kelas
        self.nis = nim

    def naikKelas(self):
        self.kelas = kelas + 1

adi = Siswa("Adi", "Laki-laki", "20", "6", "4321")

print(adi.umur)

adi.naikKelas()
print(adi.kelas)