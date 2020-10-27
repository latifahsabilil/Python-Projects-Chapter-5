#Latihan1Chapter5
#5
kodeKaryawan = int(input('Masukkan kode karyawan :'))
namaKaryawan = input('Masukkan nama karyawan :')
golongan = input('Masukkan golongan :')
status = input('Masukkan status (1: menikah, 2: blm) : ')
if(status == '1') :
    JumlahAnak = int(input('Masukkan Jumlah Anak :'))
    TunjanganMenikah = 10 / 100
    TunjanganAnak = 5 / 100 * JumlahAnak
    StatusMenikah = 'Sudah Menikah'
else:
    JumlahAnak = 0
    TunjanganMenikah = 0
    TunjanganAnak = 0
    StatusMenikah = 'Belum Menikah'

print('====================================')

print('STRUK RINCIAN GAJI KARYAWAN')

print('------------------------------------')

print('Nama Karyawan :' + namaKaryawan + '(Kode Karyawan :' + str(kodeKaryawan) + ')')
print('Golongan :' + golongan)
print('Status Menikah :' + StatusMenikah)
print('Jumlah Anak :' + str(JumlahAnak))

print('------------------------------------')

if(golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JumlahTunjanganMenikah = 10000000 * TunjanganMenikah
    JumlahTunjanganAnak = 10000000 * TunjanganAnak
    GajiKotor = 10000000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(golongan == 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JumlahTunjanganMenikah = 8500000 * TunjanganMenikah
    JumlahTunjanganAnak = 8500000 * TunjanganAnak
    GajiKotor = 8500000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2. / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(golongan == 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JumlahTunjanganMenikah = 7000000 * TunjanganMenikah
    JumlahTunjanganAnak = 7000000 * TunjanganAnak
    GajiKotor = 10000000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 1.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(golongan == 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JumlahTunjanganMenikah = 5500000 * TunjanganMenikah
    JumlahTunjanganAnak = 5500000 * TunjanganAnak
    GajiKotor = 5500000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 1.0 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
print('Gaji Pokok : Rp' + str(GajiPokok))
print('Tunjangan Menikah : Rp' + str(JumlahTunjanganMenikah))
print('Tunjangan Anak : Rp' + str(JumlahTunjanganAnak))

print('------------------------------------')

print('Gaji Kotor : Rp' + str(GajiKotor))
print('Potongan (' + str(Potongan) + '%): Rp' + str(JumlahPotongan))

print('------------------------------------')

print('Gaji Bersih : Rp' + str(GajiBersih))
