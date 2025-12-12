"""
#14-dars: Lug'at (Dictionary)
#Created on Sun Sep 21 23:00:08 2025
#author: Sherjahongir
"""


car_0 = {'model':'ferrari','rang':'qizil'}
print(car_0['model'])
print(car_0['rang'])

print("\n")

en_uz = {'apple':'olma', 'apricote':"o'rik", 'banana':"banan"}
print(en_uz['apricote'])

#Natijasi
#print(en_uz)
#{'apple': 'olma', 'apricote': "o'rik", 'banana': 'banan'}
#print(en_uz['apple'])
#olma

print("\n")

mevalar = {'olma':10000, 'tarvuz':8000, 'qovun':12000}
print(f"Olma narxi {mevalar['olma']} so'm"
      f"\ntarvuz narxi {mevalar['tarvuz']} so'm")

#Natijasi
#Olma narxi 10000 so'm
#print(mevalar['qovun'])
#12000

print("\n")

talaba_0 = {'ism':'pardayev elchin', 'yosh':'21', 't_yil':'2004'}
print(f"{talaba_0['ism'].title()},\
      \n{talaba_0['t_yil']}-yilda tug'ilgan,\
      {talaba_0['yosh']} yoshda")

#Yangi kalit so'zlar qo'shish.
talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'geografiya'

print("\n")

#Qiymatni yangilash

talaba_0['yosh'] = 19
#Natijasi
#print(talaba_0)
#{'ism': 'pardayev elchin', 'yosh': 19, 't_yil':
#'2004', 'kurs': 4, 'fakultet': 'geografiya'}

#Malumotni o'chirish
del talaba_0['yosh']
print(talaba_0)
#Bunda yoshni o'chirib tashladik, 
#buni consolda ham del bilan o'chirsak bo'ladi


telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':"mi 10 pro",
    'anvar':'pixel 3xl'
    }
print(f'Bolalar {telefonlar} telefonini ishlatadi' )
#Natijasi
#telefonlar['ali']
#Out[26]: 'iphone x'
#telefonlar['anvar']
#Out[27]: 'pixel 3xl'

print("\n")

#get
meva = en_uz.get('pineapple', 'Bunday mahsulot mavjud emas')
print(meva)

#Ntijasi
#Bunday mahsulot mavjud emas
#Yiki apple deb to'g'irlab yozsak olmani ni chiqaradi
#olma
















