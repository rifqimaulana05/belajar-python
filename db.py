import sqlite3

class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.id = nim
        self.nama = nama
        self.jurusan = jurusan
        self.nilai = 0

class Dosen:
    def __init__(self, nip, nama, mata_kuliah):
        self.id = nip
        self.nama = nama
        self.mata_kuliah = mata_kuliah

def buat_database():
    conn = sqlite3.connect('universitas.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id TEXT PRIMARY KEY,
            nama TEXT,
            jurusan TEXT,
            nilai INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dosen (
            id TEXT PRIMARY KEY,
            nama TEXT,
            mata_kuliah TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mahasiswa_id TEXT,
            nama TEXT,
            mata_kuliah TEXT,
            nilai INTEGER,
            FOREIGN KEY (mahasiswa_id) REFERENCES mahasiswa(id)
        )
    """)

    conn.commit()
    conn.close()


def tambah_mahasiswa(mhs):
    conn = sqlite3.connect('universitas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mahasiswa VALUES (?, ?, ?, ?)',
                   (mhs.id, mhs.nama, mhs.jurusan, mhs.nilai))
    conn.commit()
    conn.close()

def tambah_dosen(dsn):
    conn = sqlite3.connect('universitas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dosen VALUES (?, ?, ?)',
                   (dsn.id, dsn.nama, dsn.mata_kuliah))
    conn.commit()
    conn.close()

def tambah_nilai(mahasiswa_id, mata_kuliah, nilai):
    conn = sqlite3.connect('universitas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO nilai (mahasiswa_id, mata_kuliah, nilai) VALUES (?,?,?)',
                   (mahasiswa_id, mata_kuliah, nilai))
    conn.commit()
    conn.close()

def lihat_nilai(mahasiswa_id):
    conn = sqlite3.connect('universitas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, mata_kuliah, nilai FROM nilai WHERE mahasiswa_id=?', (mahasiswa_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    buat_database()
    
    mhs = Mahasiswa("M001", "Laba", "Matematika Disktrit")
    dsn = Dosen("D001", "Made", "Ekonomi")

    tambah_dosen(dsn)
    tambah_mahasiswa(mhs)
    

    print(lihat_nilai(mhs.id))