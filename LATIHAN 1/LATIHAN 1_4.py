#Latihan1
#4

kode = input('Masukkan kode karyawan :')
nama = input('Masukkan nama karyawan :')
golongan = input('Masukkan golongan :')

print('====================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('------------------------------------')
print('Nama Karyawan :' + nama + '(Kode Karyawan :' + str(kode) + ')')
print('Golongan:' + golongan)

print('------------------------------------')

if(golongan == 'A') :
    Gajipokok = 10000000
    Potongan = 2.5
    JumlahPotongan = Gajipokok*Potongan/100
    Gajibersih = Gajipokok - JumlahPotongan
elif(golongan == 'B') :
    Gajipokok = 8500000
    Potongan = 2.0
    JumlahPotongan = Gajipokok*Potongan/100
    Gajibersih = Gajipokok - JumlahPotongan
elif(golongan == 'C') :
    Gajipokok = 7000000
    Potongan = 1.5
    JumlahPotongan = Gajipokok*Potongan/100
    Gajibersih = Gajipokok - JumlahPotongan
elif(golongan == 'D') :
    Gajipokok =  5500000
    Potongan = 1.0
    JumlahPotongan = Gajipokok*Potongan/100
    Gajibersih = Gajipokok - JumlahPotongan
print('Gaji Pokok : Rp' + str(Gajipokok))
print('Potongan (' + str(Potongan) + '%): Rp' + str(JumlahPotongan))
print('------------------------------------ -')
print('Gaji Bersih : Rp' + str(Gajibersih))
