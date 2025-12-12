# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 08:35:57 2025

@author: Owner
"""

 # kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni ekan uff.')
    
# print("\n")


# print("Mijoz ovqatlandi")
# narx = 15000 # mijoz 15000 so'mga taom oldi
# choy = False # mijoz choy olmadi
# salat = True # mijoz salat oldi
# if choy and salat: #choy ham salat ham olgan bo'lsa
#  narx = narx + 10000# narxga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salad olgan bo'lsa
#  narx = narx + 5000 # narxga 5000 so'm qo'shamiz
#  print(f"Jami {narx} so'm") # yakuniy narxni chiqaramiz


#  print("\n")   
 
# narx = 15000 # mijoz 15000 so'mga ovqat oldi
# choy = True
# salat = False
# non = True 
# kompot = False
# assorti = True # Bularning o'rniga 1 or 0 qo'ysak ham bo'ladi
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
 
# if choy: # agar choy olsa
#   print("Mijoz choy oldi.")
#   narx = narx + 3000
  
# if salat: # agar salat olsa
#  print("Mijoz salat oldi.")
#  narx = narx + 5000
   
# if non: # agar non olsa
#  print("Mijoz non oldi.")
#  narx = narx + 2000
    
# if kompot: # agar kompot olsa
#  print("Mijoz kompot oldi.")
#  narx = narx + 5000
     
# if assorti: # agar assorti olsa
#  print("Mijoz assorti oldi.")
#  narx = narx + 15000
#  print(f"Umumiy xarajatlar: {narx} so'm")

#  menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")



 # print("Yaqin do'slaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != 'ha':
#         break
    
# print("Do'slaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narx':narxi}
#     return avto
# print("Saytimizda avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # Salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ",end=' ')
#     kompaniya=input("\nIshlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narxi=input("Narxi: ")
#     # Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
#     # Lug'at shakillantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
#     # Yana avto qo'shish-qo'shmasligini so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()} Yili:"
#           f"{avto['yil']}. {korobka} korobka. Narxi: {narx}")



 # print("New Project math moduli\n")

 # import math # Biz buni docs.python.org dan import qilib olib keldik
 # # matematik amallarni bajaradigan funksiya.
 # x=400
 # print(math.sqrt(x)) # sqrt - bu ildizini chiqaradi 400 ni.
 # print(math.pow(5,3)) # pow - bu darajasi degani bu yerda 5 ning 3 darajasi(kubi)
 # print(math.pi) # Bu pi ning qiymatini aniq ko'rsatib beradi 3.14 
 # print(math.log2(8)) # bu logorifmni hisoblaydi bunda 2 asosli log hisoblandi
 # print(math.log10(100)) # 10 asosli log hisoblandi
# yangi loyxa o'quvchilarniimtihonda o'tkazsak bo'ladi yani matematik 
# savollar bilan hamda yangi vazifalar ham qo'shamiz.


# import random as r  # Bu yerda randomni qayta r deb nomlab olayabmiz va buning
# # vazifasi tasodifiy raqam yoki ismlarni tanlaydi.
# son = r.randint(0,100) # bu yerda 0 dan 100 gacha tasodifiy raqam tanlaydi.
# print(son)










