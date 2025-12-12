# -*- coding: utf-8 -*-
"""
23-dars: MODULLAR.
Created on Thu Sep 25 09:49:34 2025
@author: Sherjahongir
"""

def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narx':narxi}
    return avto



def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida
    ma'lumotlarni bitt"""
    avtolar=[] # Salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting ",end=' ')
        kompaniya=input("\nIshlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narxi=input("Narxi: ")
    
    
    
    
        # Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
        # Lug'at shakillantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
        # Yana avto qo'shish-qo'shmasligini so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
    return avtolar



def info_print(avto_info):
     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga
     chiqaruvchi funksiya"""
     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].title()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narx']}$")
    
    








