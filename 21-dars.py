# -*- coding: utf-8 -*-
"""
21-dars: FUNKSIYAGA RO'YXAT UZATISH.
Created on Thu Sep 25 06:25:49 2025
@author: Sherjahongir
"""


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting\n>>>")
        baholar[ism]=int(baho)
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:]) # Biz [:] bu amalni bajarmasak talabalar degan 
# ro'yxatdan kopiya emas balki ko'chirib baholar degan jadvalga joylaydi 
# so'ngra talabalar ro'yxatida hech narsa qolmaydi. Lekin [:] bu amalni 
# qo'shganimiz uchun har ikkisida ham kiritgan jadval ro'yxati saqlanib turadi.
print(baholar)




# Bu yerda console da bajarilgan ishlar

#print(talabalar)
#['ali', 'vali', 'hasan', 'husan']

#talabalar2 = talabalar # talabalar dan nusxa olindi talabalar2 ga.

#print(talabalar2)
#['ali', 'vali', 'hasan', 'husan']

#talabalar2.pop() # pop bilan bittasini chiqarib tashladik
#Out[15]: 'husan'

#print(talabalar2)
#['ali', 'vali', 'hasan']

#print(talabalar) # Hamda bu chiqarganimiz talabalar ga ham tasir qildi
#['ali', 'vali', 'hasan']

# Chunki buning sababi ikkisi ham bitta jadvalga ulangan ammo ikkta o'zgaruvchi
 # orqali.





































































































