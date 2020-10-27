from random import randint

i = 0
while True:
    bil = randint(0,10)
    print(bil)
    i = i + 1
    if bil == 5:
        break
print('Jumlah perulangan :' + str(i))
