nama = str(input("Masukan Nama : "))
nim = int(input("Masukan NIM : "))
pinjaman = int(input("Masukkan pinjaman : "))

if cicilan == "1 tahun":
    bunga = (0.07/12)*pinjaman
    total = (pinjaman + bunga)/12
elif cicilan == "2 tahun":
    bunga = (0.13)
