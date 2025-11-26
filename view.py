from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

class View:

    def tampil_mahasiswa(self, data):
        console.print("\n[bold cyan]=== DATA MAHASISWA ===[/]\n")

        if not data:
            console.print("[yellow]Belum ada data mahasiswa.[/]")
            return

        table = Table(title="Daftar Mahasiswa", box=box.DOUBLE_EDGE, style="bold white")
        table.add_column("ID", style="bold yellow")
        table.add_column("Nama", style="bold green")
        table.add_column("Jurusan", style="bold magenta")

        for row in data:
            table.add_row(row[0], row[1], row[2])

        console.print(table)

    def tampil_dosen(self, data):
        console.print("\n[bold green]=== DATA DOSEN ===[/]\n")

        table = Table(title="Data Dosen", box=box.ROUNDED, style="white")
        table.add_column("NIP", style="bold yellow")
        table.add_column("Nama", style="bold cyan")
        table.add_column("Mata Kuliah", style="bold magenta")

        for d in data:
            table.add_row(d[0], d[1], d[2])

        console.print(table)

    def tampil_nilai(self, nama, data):
        console.print(f"\n[bold magenta]=== NILAI {nama} ===[/]\n")

        table = Table(title=f"Nilai {nama}", box=box.SIMPLE_HEAVY, style="white")
        table.add_column("Mata Kuliah", style="bold yellow")
        table.add_column("Nilai", style="bold green")

        for n in data:
            table.add_row(n[0], str(n[1]))

        console.print(table)
