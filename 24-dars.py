# -*- coding: utf-8 -*-
"""
24-dars: FUNKSIYALAR SO'NGISO'Z
Created on Thu Sep 25 23:18:10 2025
@author: Sherjahongir
"""


import math

uzunlik = lambda pi, r : 2*pi*r # uzunlik bu bu yerda identifikatr deyiladi
print(uzunlik(math.pi,10))
# aylana uzunligi hisoblandi va pi qiymatini yuqoridagi math dan import qildi.

print("\n")

kvadrat = lambda x, y : x ** y # kvadrat bu bu yerda identifikatr deyiladi
print(kvadrat(3, 2)) # Bu yerda 3 ning 2 chi darajasi hisoblandi.

print("\n")

def daraja(n):
    return lambda x : x**n
# Bunda daraja degan funksiya yaratildi va return lambda bilan qaytarib nomalum
# yani x qiymat oladi hamda bu x ni n chi darajaga oshiradi. hamda darajalarni
# hisoblaydi pasdagi amallarga qarab.
kvadrat = daraja(2) # Bu istalgan sonning kvadratini hisoblaydi.
#Narijasi consoledagi
#kvadrat(4)
#Out[35]: 16
#kvadrat(9)
#Out[36]: 81


kub = daraja(3) # Bu kubini hisoblaydi
# Natijasi
#kub(3)
#Out[40]: 27
#kub(5)
#Out[41]: 125

print(f"3-ning kvadrati {kvadrat(3)} ga, "
      f"kubi {kub(3)} ga teng")
    
print("\n")


from math import sqrt # sqrt bu kvadrat ildiz hisoblaydigan funksiya.

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar)) # o'sha sonlarni sqrt yani ildizini hisobla,
# va map obyekt qaytarish orqali ildizlar ro'yxatini chiqar.
print(ildizlar)

print("\n")

def daraja2(x): # daraja2 degan funksiya yaratildi.
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x # O'zini o'ziga ko'paytirib qaytaradi
print(list(map(daraja2,sonlar))) # Yuqoridagi 1 dan 10 gacha sonlar ro'yxatini
# daraja2 da kvadratga oshiradi va map bilan chiqaradi.


print("\n")
# Lekin lambada bilan buning qisqaroq usuli mavjud.

kvadratlar = list(map(lambda x: x*x,sonlar))
print(kvadratlar)

# Bu yerda lambda da qandaydir x funksiya yaratilib, bu namalum son yani x ni 
# yana o'ziga ko'paytiramiz va uning kvadrati hosil bo'ladi.
# Aynan lambda da funksiya nomi bo'lmagani uchun ham uni nomsiz funksiya deydi.

print("\n")


a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b)) # Tahlil: lambda x va y degan 2 ta qiy-
# mat qabul qiladi va ularni (x+y) bir-biriga qo'shadi hamda shu qiymat a va b. 
print(a_plus_b)
# Bu yerda 4 ga 7 ni, 5 ga 8 ni, 6 ga 9 ni qo'shadi.

print("\n")


import random as r

sonlar = r.sample(range(100),10) # 100 gacha sonlardan tasodifiy 10 ta tanlaydi.
print(sonlar)
# 1-usul
def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaradi"""
    return x%2==0 # (%) bu amal bilan juft yoki toq sonligi tekshiriladi.
# ikkiga bo'linadi qoldiq 0 bo'lsa juft aks holda toq son bo'ladi.
juft_sonlar = list(filter(juftmi,sonlar))
print(juft_sonlar)
# hamda bu yuqoridagi amallar bilan tanlangan 10 ta raqam ichidan juftlari  
# tanlab olinadi.

print("\n")
# Yoki buning lambda bilan qisqaroq usuli.
# 2-usul
juft_sonlar = list(filter(lambda x: x%2==0,sonlar))
print(juft_sonlar)

print("\n")


mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", 'ari', "banan"]
harf='a' # Istalgan boshqa harf ham qo'yishimiz mumkin
mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
print(mevalar_b) # Bunda a dan boshlanadigan mevalarni chiqaradi.

print("\n")

mevalar2 = list(filter(lambda meva:len(meva)<=4, mevalar))
print(mevalar2) # Bu uzunligi 4 harfdan oshmagan mevalarni chiqaradi.






































