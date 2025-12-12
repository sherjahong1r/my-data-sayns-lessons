"""
#7-dars: Lists
#Created on Fri Sep 19 07:36:42 2025
#author: Sherjahongir
"""


mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narxlar = [12000, 17000, 13500, 21000, -23, 12.233]
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = []

hayvonlar = ['it', 'mushuk', 'sigir', 'kuchuk', 'mushuk']

bozorlik = ["yog'", "go'sht", "piyoz", "sabzi"]


# Bular buyruqlar va ammallar consolleda qilinadigan!

#Bunda narxlarni chiqarib olishimiz mumkin.
#narxlar = [12000, 17000, 13500, 21000, -23, 12.233]
#print(narxlar[2])
#13500

#Bunda hech qanday qiymat bermasak oxiridan boshlaydi.
#print(narxlar[-1])
#12.233

#narxlar[2] + 1000
#Out[11]: 14500

#narxlar[1] + narxlar[2]
#Out[22]: 30500

#Bunda ham sonni olib tashlashimiz mumkin remove bilan.
#narxlar = [12000, 17000, 13500, 21000, -23, 12.233]
#narxlar.remove(-23)
#narxlar
#Out[62]: [12000, 17000, 13500, 21000, 12.233]

#Bunda narxlarni qo'shishimiz va boshqa amallar qilishimiz mumkin.
#narxlar[0] + narxlar[0] + 8000
#Out[63]: 32000
#narxlar[0] = narxlar[0] + 8000
#narxlar
#Out[65]: [20000, 17000, 13500, 21000, 12.233]


#Bunda upper, lower, title kabilar bilan shriftini o'zgartiramiz so'zlarning.
#print(mevalar[2].upper())
#SHAFTOLI

#Bunda mevalar sonini yana ko'paytirishimiz mumkin.
#mevalar[0] = 'uzum'
#print(mevalar)
#['uzum', 'anjir', 'shaftoli', "o'rik"]

#Bunda faqat oxiriga qo'shamiz.
#mevalar.append('qovun')
#mevalar
#Out[15]: ['uzum', 'anjir', 'shaftoli', "o'rik", 'qovun']

#Bunda faqat boshiga qo'shamiz.
#mevalar.insert(0, "banan")
#print(mevalar)
#['banan', 'uzum', 'anjir', 'shaftoli', "o'rik", 'qovun']

#Bunda mevani hohlagan joyimizga qo'shimiz mumkin raqam bilan
#qiymati berilgan holda.
#mevalar.insert(3, "mango")
#print(mevalar)
#['banan', 'uzum', 'anjir', 'mango', 'shaftoli', "o'rik", 'qovun']

#bunda conslda jadval qilish.
#cars = []
#cars.append("jentra")
#cars.append("kaptiva")
#cars.append("spark")
#cars.append("nexia")
#print(cars)
#['jentra', 'kaptiva', 'spark', 'nexia']

#Bunda biz del orqali so'zlarni ro'yxatdan olishimiz mumkin.
#del cars [0]
#print(cars)
#['kaptiva', 'spark', 'nexia']

#Bunda bir so'z o'rniga boshqasini qo'yishimiz mumkin insert orqali.
#cars.insert(0, 'lasetti')
#print(cars)
#['lasetti', 'kaptiva', 'spark', 'nexia']

#Bunda uzun ro'yxat bo'lganda orasidan hohlaganimizni o'chiramiz
# remove bilan.
#cars.remove("spark")
#print(cars)
#['lasetti', 'kaptiva', 'nexia']

#Bunda ikkita bir xil nom bo'lsa remove bilan birinchi kelganini olib
#tashlashimiz mumkin.
#hayvonlar
#Out[49]: ['it', 'mushuk', 'sigir', 'kuchuk', 'mushuk']
#hayvonlar.remove("mushuk")
#print(hayvonlar)
#['it', 'sigir', 'kuchuk', 'mushuk']

#Bunda pop buyrug'i bilan ichidan sug'irib olishimiz mumkin
#hamda agar index berilmasa oxiridagini o'chirib tashlaydi.
#print(bozorlik)
#["yog'", "go'sht", 'piyoz', 'sabzi']
#mahsulot = bozorlik.pop(1)
#print(mahsulot)
#go'sht
#print(bozorlik)
#["yog'", 'piyoz', 'sabzi']












