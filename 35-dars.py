"""
35-dars: Xatolar bilan ishlash. try-except. 
Created on Wed Oct 15 21:51:22 2025
@author: Sherjahongir
"""

# try - harakat qilmoq
# except - aks holda deb tarjima qilinadi

# Biz bu orqali foydalanuvchi butun son kiritmaganda consoleda xatolikni chiqarar-
# di try va except bilan bu xatoni tushunarli qilib chiqardik
# siz butun son kiritmadingiz deb.


yosh = input("Yoshingizni kiriting:")

try: # Harakat qiling debdi yosh kiritishga
    yosh = int(yosh) # Faqat butun sonni chunki int bor
except ValueError: # Yani console ValueError deb hato chiqarsa pastdagini chiqar
    print("Siz butun son kiritmadingiz")
else: # aks holda to'g'ri bo'lsa bu kodni bajar.
    print(f"Siz {2025-yosh} yilda tug'ilgansiz")

print("Dastur davom etayabdi")
print("Dastur tugadi")

print("\n")

# ZeroDivisionError:
    
# x,y=5,10
# y/(x-5)

# Natijasi
# ZeroDivisionError: division by zero # Bunday xatolik chiqaradi

x,y=5,10
try:
    y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas") # Buning tushunarli yechimi

print("\n")

mevalar = ['olma','anor','anjir','uzum']
try:
    print(mevalar[4])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")


print("\n")


user = {"username":"Sher_Jahongir",
        "status":"admin",
        "email":"admin@sher.jahongir",
        "phone":"998941334321"}  

key="tel" # username ni so'rashi kerak edi
try:
    print(f"Foydalanuvchi: {user[key]}")
except KeyError:
    print("Bunday kalit mavjud emas")

print(f"Siz bu {user['username']} foydalanuvchini qidirgan bo'lishingiz mumkin")


print("\n")


filename = "data.txt"  # Bunaday fayl mavjud emas
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"{filename} mavjud emas")
# Agar bu yerda try va except dan foydalanmaganimizda FileNotFoundError degan 
# xato chiqardi


print("\n")


import json
files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
            print(f"{filename} mavjud emas")
#        pass   # Bu buyruq ham mavjud emas faylni tashlab pastdagi mavjud 
    else:  # faylga avtomatiski o'tadi buning uchun yuqoridagi printni o'chiramiz
            print(talaba['ism'])
# Bu yerda talaba1,2,4 degan fayl yaratilganda va ularda nimadir ism ciqadi
# lekin talaba3 degan fayl mavjud bo'lmagani uchun uninig joyini tashlab
# mavjud emas deb pastdagi buyruqlarni bajaradi codni xato chiqarmasdan.
# menda hech qaysi fayl bo'lmagani uchun hammasi mavjud emas deb chiqadi.


print("\n")


n = input("Butun son kiriting: ")
try:
    n = int(n)
    x=20/n
except ValueError: # Agar foydalanuvchi butun son kiritmasa
    print("Butun son kiritmadingiz")
except ZeroDivisionError: # Agar foydalanuvchi 0 ga bo'lmoqchi bo'lsa
    print("0 ga bo'lish mumkin emas")
else:
    print(f"x={x}")

# Bir vaqtning o'zida bir nechta except deb chiqishi mumkin bo'lgan 
# xatoliklarning oldini olish mumkin.

# NATIJASI
# Butun son kiriting: 2.2
# Butun son kiritmadingiz
# Butun son kiriting: 0
# 0 ga bo'lish mumkin emas
# Butun son kiriting: 5
# x=4.0


print("\n")


# try va except dan ko'ra yana maqulroq variant yuqoridagi amal uchun.

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():  # Bu faqat butun son qabul qiladi
        yosh = int(yosh)
        break 
print(f"Siz {2025-yosh} yilda tug'ilgansiz")

# Butun son kiritilmaguncha dastur to'xtamaydi.

# '20'.isdigit()  # butun son bo'lsa true 
# Out[21]: True
# '20,5'.isdigit()
# Out[22]: False  # aks holda false deb chiqaradi consoleda tekshirganimizda.
# 'besh'.isdigit()
# Out[23]: False












