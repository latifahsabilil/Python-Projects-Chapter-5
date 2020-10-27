#Latihan1
#1
indo = int(input('Nilai Bahasa Indonesia :'))
if (indo >= 0 and indo <= 100):

    mtk = int(input('Nilai Matematika :'))
if (mtk >= 0 and mtk <= 100):

    ipa = int(input('Nilai IPA :'))
if (ipa >= 0 and ipa <= 100):
           
 print('==========================')

if(indo>60 and ipa>60 and mtk>70):
           print ('LULUS')
else:
    print ('Tidak Lulus')
