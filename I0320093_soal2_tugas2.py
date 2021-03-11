print("====BIODATA====")

#BIODATA
Nama = "Sekar Salsabila Santosa"
Nama_Panggilan = "Sekar"
NIM = "I0320093"
Tanggal_Lahir = "1 November 2001"
Program_Studi = "Teknik Industri"
Universitas = "Universitas Sebelas Maret"
Angkatan_Universitas = "2020"
SMA = "SMAN 1 Semarang"
Alamat = "Jalan Menoreh Utara XI Nomor 22, Semarang, Jawa Tengah"
Hobi = "Menyanyi, Mendengarkan Musik, dan Menonton Film dan Drama"
Instagram = "@sekarsabill"
ID_Line = "sekarsabil"
Tempat_Lahir = "Semarang"
Tinggi_Badan = 159.5
Makanan_Favorit = "Seafood"
Minuman_Favorit = "Kopi"

#Variabel Umur
Bulan_Sekarang = 3
Bulan_Lahir = 11
Tahun_Sekarang = 2021
Tahun_Lahir = 2001

#Menghitung Usia (Tahun dan Bulan)
Usia_Dalam_Bulan = ((12 * Tahun_Sekarang + Bulan_Sekarang) - (12 * Tahun_Lahir + Bulan_Lahir))
Usia_Tahun = int(Usia_Dalam_Bulan/12)
Usia_Bulan = Usia_Dalam_Bulan % 12
Usia = str(Usia_Tahun) + " Tahun " + str(Usia_Bulan) + " Bulan"

#Tampilan Biodata di Layar
print("Nama :", Nama)
print("Nama Panggilan :", Nama_Panggilan)
print("NIM :", NIM)
print("Tanggal Lahir :", Tanggal_Lahir)
print("Program Studi :", Program_Studi)
print("Universitas :", Universitas)
print("Angkatan Universitas :", Angkatan_Universitas)
print("SMA :", SMA)
print("Alamat :", Alamat)
print("Hobi :", Hobi)
print("Instagram :", Instagram)
print("ID Line :", ID_Line)
print("Tempat Lahir :", Tempat_Lahir)
print("Tinggi Badan :", Tinggi_Badan, "cm")
print("Makanan Favorit :", Makanan_Favorit)
print("Minuman Favorit :", Minuman_Favorit)
print("Usia :", Usia)