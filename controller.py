from model import Database
from view import View
from rich.console import Console

console = Console()

class Controller:
    def __init__(self):
        self.db = Database()
        self.view = View()

    def tambah_mahasiswa(self):
        id = input("ID Mahasiswa: ")
        nama = input("Nama: ")
        jurusan = input("Jurusan: ")
        self.db.tambah_mahasiswa(id, nama, jurusan)
        console.print("[bold green]✔ Mahasiswa berhasil ditambahkan![/]")

    def tampilkan_mahasiswa(self):
        data = self.db.get_mahasiswa()
        self.view.tampil_mahasiswa(data)

    def update_mahasiswa(self):
        id = input("ID mahasiswa: ")
        nama = input("Nama baru: ")
        jurusan = input("Jurusan baru: ")
        self.db.update_mahasiswa(id, nama, jurusan)
        console.print("[bold green]✔ Data berhasil diperbarui![/]")

    def delete_mahasiswa(self):
        id = input("ID yang dihapus: ")
        self.db.delete_mahasiswa(id)
        console.print("[bold red]✔ Mahasiswa berhasil dihapus![/]")



    def tambah_dosen(self):
        id = input("NIP: ")
        nama = input("Nama Dosen: ")
        matkul = input("Mengajar Mata Kuliah: ")
        self.db.tambah_dosen(id, nama, matkul)
        console.print("[bold green]✔ Dosen berhasil ditambahkan![/]")

    def tampilkan_dosen(self):
        data = self.db.get_dosen()
        self.view.tampil_dosen(data)



    def beri_nilai(self):
        mhs = input("ID mahasiswa: ")
        matkul = input("Mata kuliah: ")
        nilai = int(input("Nilai: "))
        self.db.beri_nilai(mhs, matkul, nilai)
        console.print("[bold yellow]✔ Nilai berhasil diberikan![/]")

    def tampilkan_nilai(self):
        mhs = input("ID mahasiswa: ")
        mahasiswa = [x for x in self.db.get_mahasiswa() if x[0] == mhs]

        if not mahasiswa:
            console.print("[bold red]Mahasiswa tidak ditemukan![/]")
            return

        nama = mahasiswa[0][1]
        nilai = self.db.get_nilai(mhs)
        self.view.tampil_nilai(nama, nilai)
