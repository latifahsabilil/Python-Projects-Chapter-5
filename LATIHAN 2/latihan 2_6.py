#Latihan2
#5

print('Hai...nama saya Mr.Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!!')
tebakan = int(input('Tebakan anda :'))
kurangipoin = 0

while True:
      if (tebakan<10) :
            print('Hehehe... Bilangan tebakan anda terlalu kecil')
            tebakan = int(input('Tebakan anda :'))
            kurangipoin+=2
      if(tebakan>10) :
            print('Hehehe... Bilangan tebakan anda terlalu besar')
            tebakan = int(input('Tebakan anda :'))
            kurangipoin+=2
      if (tebakan==10) :
            print('Yeeee... Bilangan tebakan anda BENAR :-)')
            score=100-kurangipoin
            print('Score anda : ' + str(score))
            break

