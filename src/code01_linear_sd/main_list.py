from services.mahasiswa_reader import MahasiswaReader
import time

def main():
    # Membuat objek pembaca CSV
    reader = MahasiswaReader("data/data_mahasiswa_dummy_200.csv")

    # Membaca data dan menghasilkan list mahasiswa
    list_mahasiswa = reader.baca_data()
    #list_mahasiswa = reader.baca_data_as_linked_list()

    # Menampilkan beberapa data
    #for mhs in list_mahasiswa:
    #    mhs.info()

    # Menampilkan data indeks ke 99
    waktu_mulai = time.perf_counter() # Cek waktu awal
    list_mahasiswa[98].info()
    #list_mahasiswa.at(98).info()
    waktu_selesai = time.perf_counter() # Cek waktu akhir

    durasi = waktu_selesai - waktu_mulai
    print("Waktu: ",durasi," detik")

if __name__ == "__main__":
    main()