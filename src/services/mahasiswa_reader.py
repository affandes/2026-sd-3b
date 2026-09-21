import csv
from models.mahasiswa import Mahasiswa
from models.linked_list import LinkedList


class MahasiswaReader:
    def __init__(self, nama_file):
        self.nama_file = nama_file

    def baca_data(self):
        daftar_mahasiswa = []

        file = open(self.nama_file, "r")

        reader = csv.DictReader(file)

        for baris in reader:
            mahasiswa = Mahasiswa(
                int(baris["indeks"]),
                baris["nim"],
                baris["nama"],
                baris["prodi"],
                float(baris["ipk"])
            )

            daftar_mahasiswa.append(mahasiswa)

        file.close()

        return daftar_mahasiswa

    
    def baca_data_as_linked_list(self):
        daftar_mahasiswa = LinkedList()

        file = open(self.nama_file, "r")

        reader = csv.DictReader(file)

        for baris in reader:
            mahasiswa = Mahasiswa(
                int(baris["indeks"]),
                baris["nim"],
                baris["nama"],
                baris["prodi"],
                float(baris["ipk"])
            )

            daftar_mahasiswa.add_last(mahasiswa)

        file.close()

        return daftar_mahasiswa