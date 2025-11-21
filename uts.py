from colorama import Fore, Back, Style, init
from tabulate import tabulate
import sqlite3
init(autoreset=True)


class Orang:
    def __init__(self, nama, id):
        self.nama = nama
        self.id = id

    def tampil_info(self):
        print(f"{Fore.YELLOW}Nama: {self.nama}")
        print(f"{Fore.YELLOW}ID: {self.id}")



class Nilai:
    def __init__(self, mata_kuliah, nilai):
        
        self.__mata_kuliah = mata_kuliah
        self.__nilai = nilai

    def tampilkan(self):
        print(self.__mata_kuliah, ":", self.__nilai)

    def get_nilai(self):
        return self.__nilai



class Mahasiswa(Orang):
    def __init__(self, nama, nim, jurusan):
        super().__init__(nama, nim)   
        self.jurusan = jurusan
        self.__nilai_list = []        

    def tambah_nilai(self, nilai):
        self.__nilai_list.append(nilai)

    def lihat_nilai(self):
        print("\nDaftar Nilai", self.nama, f"({self.jurusan})")
        if len(self.__nilai_list) == 0:
            print("Belum ada nilai.")
        else:
            for n in self.__nilai_list:
                n.tampilkan()

    
    def tampil_info(self):
        print("=== Data Mahasiswa ===")
        print(f"{Fore.YELLOW}Nama: {self.nama}")
        print(f"{Fore.YELLOW}NIM: {self.id}")
        print(f"{Fore.YELLOW}Jurusan: {self.jurusan}")



class Dosen(Orang):
    def __init__(self, nama, nip, mata_kuliah):
        super().__init__(nama, nip)
        self.mata_kuliah = mata_kuliah

    def beri_nilai(self, mahasiswa, angka):
        
        nilai_baru = Nilai(self.mata_kuliah, angka)
        mahasiswa.tambah_nilai(nilai_baru)
        print(f"{Fore.BLUE}{self.nama} memberi nilai {angka} ke {mahasiswa.nama} untuk {self.mata_kuliah}")

    def tampil_info(self):
        print("=== Data Dosen ===")
        print(f"{Fore.RED}Nama: {self.nama}")
        print(f"{Fore.RED}NIP: {self.id}")
        print(f"{Fore.RED}Mengajar: {self.mata_kuliah}")



if __name__ == "__main__":
    
    mhs1 = Mahasiswa("Rifqi", "M001", "Sistem Informasi")
    mhs2 = Mahasiswa("Andi", "M002", "Informatika")

    dosen1 = Dosen(f"{Fore.GREEN}Bu Sari", f"{Fore.GREEN}D001", f"{Fore.GREEN}Pemrograman Python")

    mhs1.tampil_info()
    mhs2.tampil_info()
    dosen1.tampil_info()

    dosen1.beri_nilai(mhs1, 90)
    dosen1.beri_nilai(mhs2, 85)

    mhs1.lihat_nilai()
    mhs2.lihat_nilai()

    header = [f"{Fore.CYAN}NAMA", "NIM", "JURUSAN", "NILAI"]

    data = [
        [mhs1.nama, mhs1.id, mhs1.jurusan, mhs1._Mahasiswa__nilai_list[0].get_nilai()], 
        [mhs2.nama, mhs2.id, mhs2.jurusan, mhs2._Mahasiswa__nilai_list[0].get_nilai()]
    ]

    print(Fore.BLUE +"\nTABEL DATA MAHASISWA:")
    print(tabulate(data, headers=header, tablefmt="double_grid"))

    header = [f"{Fore.GREEN}NAMA", "NIP", "MATAKULIAH"]
    data = [
        [dosen1.nama, dosen1.id, dosen1.mata_kuliah]
    ]
    print(Fore.MAGENTA + "\nTABEL DATA DOSEN:")
    print(tabulate(data, headers=header, tablefmt="heavy_grid"))
