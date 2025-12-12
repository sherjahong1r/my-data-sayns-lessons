"""
#15-dars: Lug'at bilan ishlash
#Created on Mon Sep 22 10:36:28 2025
#author: Sherjahongir
"""


talaba_0 = {
    'ism':'alijon',
    'familya':'valijonov',
    'yosh':22,
    'fakultet':'geografiya',
    'kurs':4
    }

#print(talaba_0.items())

for key, value in talaba_0.items():
    print(f"Kalit: {key}")
    print(f"Qiymat: {value} \n")

print("\n")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'}

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
    
print("\n")
    
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

bozorlik = ['anor','uzum','non','baliq','shaftoli']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

#print(mahsulotlar)
#{'olma': 10000, 'anor': 20000, 'uzum': 40000, 'anjir': 25000, 'shaftoli': 30000}

#Anor 20000 so'm
#Uzum 40000 so'm

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
#Bu yerda not bilan yo'q buyumlarni olib keling deb buyruq berilmoqda.

print("\n")

print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
#Bu yerda sorted buyrug'i alifbe tartibida tartiblaydi

print("\n")

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
#Bu yerda values bilan telefon rusumlarini chiqaramiz yuqoridagi 
#telefonlar jadvalidan.

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
#Bu yerda rusimi bir xil bo'lgan tellarni ham yana qayta chiqaradi
    
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)
#Bu yerda esa set buyrug'i bilan faqat bir xil rusumlilarni chiqaradi
# Set ham type hisoblanib bir jadvalda 2 3 xil narsalar takrorlangan
#bo'lsa faqat bittasini chiqaradi.











































