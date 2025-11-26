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

class Database:
    def __init__(self, db_name='universitas.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.buat_tabel()

    def buat_tabel(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mahasiswa (
                id TEXT PRIMARY KEY,
                nama TEXT,
                jurusan TEXT,
                nilai INTEGER
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dosen (
                id TEXT PRIMARY KEY,
                nama TEXT,
                mata_kuliah TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS nilai (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mahasiswa_id TEXT,
                mata_kuliah TEXT,
                nilai INTEGER
            )
        """)

        self.conn.commit()

    def tambah_mahasiswa(self, id, nama, jurusan):
        self.cursor.execute("INSERT INTO mahasiswa VALUES (?, ?, ?)", (id, nama, jurusan))
        self.conn.commit()

    def get_mahasiswa(self):
        self.cursor.execute("SELECT * FROM mahasiswa")
        return self.cursor.fetchall()

    def update_mahasiswa(self, id, nama, jurusan):
        self.cursor.execute("UPDATE mahasiswa SET nama=?, jurusan=? WHERE id=?", (nama, jurusan, id))
        self.conn.commit()

    def delete_mahasiswa(self, id):
        self.cursor.execute("DELETE FROM mahasiswa WHERE id=?", (id,))
        self.conn.commit()



    def tambah_dosen(self, id, nama, matkul):
        self.cursor.execute("INSERT INTO dosen VALUES (?, ?, ?)", (id, nama, matkul))
        self.conn.commit()

    def get_dosen(self):
        self.cursor.execute("SELECT * FROM dosen")
        return self.cursor.fetchall()


    def beri_nilai(self, mahasiswa_id, matkul, nilai):
        self.cursor.execute("INSERT INTO nilai(mahasiswa_id, mata_kuliah, nilai) VALUES (?, ?, ?)",
                (mahasiswa_id, matkul, nilai))
        self.conn.commit()

    def get_nilai(self, mahasiswa_id):
        self.cursor.execute("SELECT mata_kuliah, nilai FROM nilai WHERE mahasiswa_id=?", (mahasiswa_id,))
        return self.cursor.fetchall()