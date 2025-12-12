"""
#10-dars: if-else shartlari va tarmoqlanish.[Tarmoqlanish]
#Created on Sat Sep 20 22:16:28 2025
#author: Sherjahongir
"""


avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']

for avto in avtolar: #avtolar ichidagi har bir avto uchun
    if avto == 'bmw':#agar avto bmw ga teng bo'lsa
        print(avto.upper()) #avto nomini hamma harfini kattalashtir
    else: #aks holda
        print(avto.title()) #avto nomi faqat birinchi harfi katta bo'lsin

#Bu ko'dlarning natijasi.
#avtolar
#Out[6]: ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
#for avto in avtolar:
#    print(avto.title())
#Audi
#Bmw
#Volvo
#Kia
#Hyundai

#avto = jadval oxiridagiga teng bo'ladi va bundan else kabi buyruqlar 
#so'ralmaydi, qolganlari uchun agar teng bo'lmasa deb avto.title beriladi.
#avtolar
#Out[14]: ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
#print(avto)
#hyundai
#avto == 'bmw'
#Out[16]: False
#avto == 'hyundai'
#Out[17]: True

#Bularni console da tekshirib ko'ramiz
#a = 5 # bu teng degan manoni anglatadi
#a == 5 # bu tengmi degani
#Out[22]: True
#a == 6
#Out[23]: False
#a != 6 # bu teng emas degan manoni anglatadi
#Out[24]: True
#a != 5
#Out[25]: False

print("\n")

ism = input('ismingiz nima?\n>>>') # foydalanuvchi ismini so'rayabdi
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa
    print(f"Uzur, {ism.title()} biz Alini kutyabmiz.")
else:
    print("Salom, Ali")
#Bu ko'dni natijasini chiqarganimizdan keyin 
#pastdagi ko'dlar natijasi chiqadi.


# Bu ko'dning natijasi.
#ismingiz nima?
#>>>ali
#Salom, Ali
#ismingiz nima?
#>>>vali
#Uzur, Vali biz Alini kutyabmiz.

print("\n")

javob = float(input("12x6 nechiga teng?>>>"))
if javob!=72:
    print("Javob xato!")
    print("To'gri javob 72 edi")
else:
    print("javob to'g'ri✓🏆🏆🏆🏆")

print("\n")

yosh = input("Butun son kiriting:")

try: # Harakat qiling debdi yosh kiritishga
    yosh = int(yosh) # Faqat butun sonni chunki int bor
except ValueError: # Yani console ValueError deb hato chiqarsa pastdagini chiqar
    print("Siz butun son kiritmadingiz")
else: # aks holda to'g'ri bo'lsa bu kodni bajar.
    print(f"Siz {2025-yosh} yilda tug'ilgansiz")

print("Dastur davom etayabdi")
print("Dastur tugadi")
   
#Natijasi
#ismingiz nima?
#>>>ali
#Salom, Ali
#12x6 nechiga teng?>>>72
#javob to'g'ri✓🏆🏆🏆🏆

print("\n")

ism = input("Ismingizni kiriting>>>")
try: 
    ism = int(ism)
except ValueError:
    print("Siz to'g'ri variant kiritingiz")
else:
    print("Siz so'z birikmasi kiritishingiz kerak")
        
print("\n")
        
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18:
    print("Xush kelibsiz!")
else:
    print('Kirish mumkin emas!')

# Natijasi
#Yoshingiz nechida?>>>17
#Kirish mumkin emas!
#Yoshingiz nechida?>>>18
#Xush kelibsiz

#yosh
#Out[50]: 17
#yosh < 18
#Out[51]: True
#yosh > 18
#Out[52]: False
#yosh <= 18
#Out[53]: True

print("\n")

login = input("Yangi login tanlang:")
if len(login)<=5: # 5 harfdan ko'proq bo'lishi kerak
    print("Login 5 harfdan ko'proq bo'lishi shart")
else:
    print("siz to'g'ri kiritingiz")
    
#Natijasi
#Yangi login tanlang:vali
#Login 5 harfdan ko'proq bo'lishi shart
#Yangi login tanlang:jahongir
#siz to'g'ri kiritiniz

print("\n")

yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2025-yil<18:
    print(f"Yoshingiz {2025-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz")

#Natijasi
#Tug'ilgan yilingizni kiriting:2013
#Yoshingiz 12da ekan.
#Kirish mumkin emas!
#Tug'ilgan yilingizni kiriting:2004
#Xush kelibsiz

print("\n")

yosh = int(input("yoshingiz nechida?>>>"))
if yosh>65: 
    print("Siz COVID-19 risk guruhida ekansiz")
else:
    print("Sog'lom hayot uchun har doim harakat qiling")
    
#Natijasi
#yoshingiz nechida?>>>67
#Siz COVID-19 risk guruhida ekansiz
#yoshingiz nechida?>>>56
#Sog'lom hayot uchun har doim harakat qiling

print("\n")

# x, y = 50, 40
# #print("x>y") if x>y else print("x<y")
# if x>y 
#     print("Siz yosh ekansiz") 
# else: 
#     print("Sizning yoshingiz katta")




















