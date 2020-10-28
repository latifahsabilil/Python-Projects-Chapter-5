#Latihan1Chapter5
#5

kode = input('Masukkan kode karyawan :')
nama = input('Masukkan nama karyawan :')
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

print('Nama Karyawan :' + nama + '(Kode Karyawan :' + str(kode) + ')')
print('Golongan :' + golongan)
print('Status Menikah :' + StatusMenikah)
print('Jumlah Anak :' + str(JumlahAnak))

print('------------------------------------')

if(golongan == 'A'):
    Gajipokok = 10000000
    Potongan = 2.5
    JumlahTunjanganMenikah = 10000000 * TunjanganMenikah
    JumlahTunjanganAnak = 10000000 * TunjanganAnak
    Gajikotor = 10000000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2.5 / 100 * Gajikotor
    Gajibersih = Gajikotor - JumlahPotongan
elif(golongan == 'B'):
    Gajipokok = 8500000
    Potongan = 2.0
    JumlahTunjanganMenikah = 8500000 * TunjanganMenikah
    JumlahTunjanganAnak = 8500000 * TunjanganAnak
    Gajikotor = 8500000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2. / 100 * Gajikotor
    Gajibersih = Gajikotor - JumlahPotongan
elif(golongan == 'C'):
    Gajipokok = 7000000
    Potongan = 1.5
    JumlahTunjanganMenikah = 7000000 * TunjanganMenikah
    JumlahTunjanganAnak = 7000000 * TunjanganAnak
    Gajikotor = 10000000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 1.5 / 100 * Gajikotor
    Gajibersih = Gajikotor - JumlahPotongan
elif(golongan == 'D'):
    Gajipokok = 5500000
    Potongan = 1.0
    JumlahTunjanganMenikah = 5500000 * TunjanganMenikah
    JumlahTunjanganAnak = 5500000 * TunjanganAnak
    Gajikotor = 5500000 + JumlahTunjanganMenikah + JumlahTunjanganAnak
    Jumlahpotongan = 1.0 / 100 * Gajikotor
    Gajibersih = Gajikotor - JumlahPotongan
print('Gaji Pokok : Rp' + str(Gajipokok))
print('Tunjangan Menikah : Rp' + str(JumlahTunjanganMenikah))
print('Tunjangan Anak : Rp' + str(JumlahTunjanganAnak))

print('------------------------------------')

print('Gaji Kotor : Rp' + str(Gajikotor))
print('Potongan (' + str(Potongan) + '%): Rp' + str(JumlahPotongan))

print('------------------------------------')

print('Gaji Bersih : Rp' + str(Gajibersih))
