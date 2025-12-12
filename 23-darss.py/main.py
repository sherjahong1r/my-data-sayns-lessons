"""
23-dars: MODULLAR.
Created on Thu Sep 25 10:56:36 2025
@author: Sherjahongir.
"""



# IMPORT QILISHNING TURLI USULLARI

import avto_info_mod # Faylni import qilib olib keldik
avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,400001)
avto_info_mod.info_print(avto1)

print("\n")

import avto_info_mod as aim # Bu as orqali biz nomini qisqartiramiz va aim boldi
avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,400002)
aim.info_print(avto1)

print("\n")

from avto_info_mod import avto_info, info_print
# aim dan ko'chirib olib kel avto_info va info_print ni degani.
# Buning natijasida modulni ham yozish shart emas to'g'ridan to'g'ri funksiyani
# yozsa bo'ladi.
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,400003)
avto2 = avto_info("chevrolet", "nexia", "oq", "mexanika", 2015,350003)
info_print(avto1)
info_print(avto2)

print("\n")

from avto_info_mod import avto_info as ainfo, info_print as iprint
# Bu orqali bir yo'li ham import ham funksiyaga boshqa nom ham beramiz as bilan.
avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,400004)
iprint(avto1)
# bu oynada ham boshqa shunday nomli funksiya bo'lganda nomini o'zgartirib 
# olib kelish qulay hisoblanadi.

print("\n")

from avto_info_mod import *
# Bu bilan aim dagi barcha funksiyalarni chaqiramiz yani avto_info, info_print,
# va avto_kirit ni ham lekin bu usul tavsiya qilinmaydi chunki juda katta chal-
# kashliklarga olib keladi chunki bunday nomli funksiya bu oynada ham
# bo'lishi mumkin.
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,400005)
info_print(avto1)

print("\n")

print("New Project math moduli\n")

import math # Biz buni docs.python.org dan import qilib olib keldik
# matematik amallarni bajaradigan funksiya.
x=400
print(math.sqrt(x)) # sqrt - bu ildizini chiqaradi 400 ni.
print(math.pow(5,3)) # pow - bu darajasi degani bu yerda 5 ning 3 darajasi(kubi)
print(math.pi) # Bu pi ning qiymatini aniq ko'rsatib beradi 3.14 
print(math.log2(8)) # bu logorifmni hisoblaydi bunda 2 asosli log hisoblandi
print(math.log10(100)) # 10 asosli log hisoblandi

print("\n")

print("random moduli\n")

import random as r  # Bu yerda randomni qayta r deb nomlab olayabmiz va buning
# vazifasi tasodifiy raqam yoki ismlarni tanlaydi.
son = r.randint(0,100) # bu yerda 0 dan 100 gacha tasodifiy raqam tanlaydi.
print(son)

print("\n")

ismlar = ['olim', 'anvar', 'hasan', 'husan', 'ali', 'vali', 'salim', 'bakir']
ism = r.choice(ismlar) # choice ismlarni tasodifiy tanlaydi.
print(ism)
print(r.choice(ism)) # Bu tasodifiy tanlangan ism ichidagi harflarni yana 
# qaytadan tasodifiy tanlaydi

print("\n")

x = list(range(0,101,5)) # 0 dan 101 gacha raqamlar 5 qadam tashlab yozilgan jadval
print(x)
print(r.choice(x))

print("\n")

# shuffle() bu jadvalni aralashtirib tashlaydigan buyruq.
x = list(range(11)) # 11 gacha sonlar ro'yxati
print(x)
r.shuffle(x)
print(x)
