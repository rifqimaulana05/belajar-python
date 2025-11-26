from controller import Controller
from rich.console import Console

console = Console()

if __name__ == "__main__":
    app = Controller()

    while True:
        console.print("""
[bold cyan]
========== MENU APLIKASI ==========
1. Tambah Mahasiswa
2. Lihat Mahasiswa
3. Update Mahasiswa
4. Hapus Mahasiswa
5. Tambah Dosen
6. Lihat Dosen
7. Beri Nilai
8. Lihat Nilai Mahasiswa
0. Keluar
[/]
""")

        pilih = input("Pilih menu: ")

        if pilih == "1": app.tambah_mahasiswa()
        elif pilih == "2": app.tampilkan_mahasiswa()
        elif pilih == "3": app.update_mahasiswa()
        elif pilih == "4": app.delete_mahasiswa()
        elif pilih == "5": app.tambah_dosen()
        elif pilih == "6": app.tampilkan_dosen()
        elif pilih == "7": app.beri_nilai()
        elif pilih == "8": app.tampilkan_nilai()
        elif pilih == "0": break
        else:
            console.print("[bold red]Pilihan tidak valid![/]")
