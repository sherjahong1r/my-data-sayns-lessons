# -*- coding: utf-8 -*-
"""
22-dars: (Moslashuvchan funksiyalar). *args va **kwargs(key.words.args).# degani
#kwargs 
Created on Thu Sep 25 08:28:59 2025
@author: Sherjahongir.
"""

# *args = ko‘p miqdordagi nomsiz argumentlar. biita yulduzcha bilan yoziladi

# **kwargs = ko‘p miqdordagi kalit=qiymat argumentlar. Bu esa ikkita.


def summa(*sonlar): # Bu yerda yulduzcha qo'yib yozish natijasida holagancha 
# sonlar (argument) kiritib hisoblasak bo'ladi.
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(4,5,6,7))

print("\n")

def summa(x,y,*sonlar): # Bu yerda kamida ikkita qiymat kiritishimiz kerak 
# x va y ga qolgani ixtiyoriy.

    return x+y+sum(sonlar)
print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(4,5,6,7))
print(summa(2,89))

print("\n")


def avto_info(kompaniya, model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info('GM', 'Malibu', rang='Qora', yil=2018)
avto2 = avto_info('Kia', 'K5', rang='Oq', yil=2016, narx=15000, korobka='avtomat')

# Bunda ham **malumotlar degani yana hohlagancha boshqa malumotlar kiritishimiz 
#mumkin va console da qo'shimcha kiritgan malumotlarimiz birinchi chiqadi 
# keyin majburiylari chiqadi.

# avto1 va avto2 deb consolega yozsak natijasini ko'rsatadi.

















































































