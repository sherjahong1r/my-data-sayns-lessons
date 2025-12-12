"""
34-dars: JSON
Created on Wed Oct 15 10:25:00 2025
@author: Sherjahongir
"""


# JSON - JavaScript Object Notation - (Malumotlarni saqlash va uzatish formati)

# Bu JSON malumotlarni bir dasturdan serverga yoki serverdan dasturga yuborishda
# qulay hisoblanadi. 

# Shuningdek yonda joylashgan bemor.json ham 34 - darsga tegishi bo'lib
# dump yordamida yangi bemor.json degan fayl yaratilgan pastda.

import json

x = 10
x_json = json.dumps(x) # dumps ning vazifasi jsonga o'tkazib beradi.
# json da int va float ni ham saqlaganimizda matn yani str ko'rinishiga o'tadi
# faqat vaqtinchalik yana boshqaga uzatib ochilganda o'z holiga qaytadi.

# Natija
# type(x)
# Out[10]: int
# print(x)
# 10
# type(x_json)
# Out[12]: str
# print(x_json)
# 10

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

# Natijasi consoledagi
# m
# Out[15]: True
# type(m)
# Out[16]: bool     # bool bu mantiqiy qiymat degani.
# print(m_json)
# true

sonlar = (12, 45, 13, 67)
sonlar_json = json.dumps(sonlar)

# Natijasi
# sonlar
# Out[19]: (12, 45, 13, 67)
# type(sonlar) 
# Out[20]: tuple # Bu yerda tuple dan Array yani [to'rtburchak qavs] 
# sonlar_json    # ko'rinishiga o'zgarayabdi buning jadvali eng pastda.
# Out[21]: '[12, 45, 13, 67]'

# Endi buning teskarisi pythone ga o'tkazamiz
# m_json
# Out[22]: 'true'
# json.loads(m_json)
# Out[23]: True
# json.loads(sonlar_json) # Bunda tuple gini bilmagani uchun list ko'rinishiga
# Out[24]: [12, 45, 13, 67] # o'tkazdi bu ham jadvalda bor.

bemor = {
    "ism": "Alijon Valiyev",
    "yosh": 30,
    "oila": True,
    "farzandlar": ("Ahmad", "Bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "panadol", "miqdori": 1.2}
        ]
    }

bemor_json = json.dumps(bemor, indent=4) # Bu yerda indent=4 degani chapdan 
# 4 qator tashlab alohida tushunarli yozadi. U bo'lmaganda matn qilib chiqarardi.
print(bemor_json)

# NATIJASI
# {
#     "ism": "Alijon Valiyev",
#     "yosh": 30,
#     "oila": true,
#     "farzandlar": [
#         "Ahmad",
#         "Bonu"
#     ],
#     "allergiya": null,
#     "dorilar": [
#         {
#             "nomi": "Analgin",
#             "miqdori": 0.5
#         },
#         {
#             "nomi": "panadol",
#             "miqdori": 1.2
#         }
#     ]
# }

# bemor.keys()
# Out[5]: dict_keys(['ism', 'yosh', 'oila', 'farzandlar', 'allergiya', 'dorilar'])
# bemor['dorilar']
# Out[6]: [{'nomi': 'Analgin', 'miqdori': 0.5}, {'nomi': 'panadol', 'miqdori': 1.2}]
# bemor['farzandlar']
# Out[7]: ('Ahmad', 'Bonu')

with open('bemor.json','w') as f: # Bunda bemor.json degan yangi fayl
    json.dump(bemor,f) #  yaratiladi dump bilan. 

bemor2 = json.loads(bemor_json) # Bunda loads bilan yana json ko'rinishdan 
# python ko'rinishiga o'tkazayapmiz.

# type(bemor_json) # json ko'rinishi
# Out[14]: str

# type(bemor2) # python ko'rinishi
# Out[12]: dict

# sonlar_json
# Out[15]: '[12, 45, 13, 67]' 
# sonlar_json[0]
# Out[20]: '['                      # json ko'rinishidan
# sonlar2 = json.loads(sonlar_json) # python ko'rinishiga o'tkazdik
# sonlar2[0]                        # consoleda loads bilan.
# Out[17]: 12
# sonlar2[3]
# Out[19]: 67

# pythondan boshqa formatlarga misol uchun jsonga yoki boshqaga o'tkazganimizda 
# loads bilan yana asl holiga qaytarish mumkin.







# import json
# import googlemaps
# from apikey import APIKEY

# ## GoogleMaps
# gmaps = googlemaps.Client(key=APIKEY)

# data = gmaps.geocode('Olmazor, Tashkent, Uzbekistan')

# # print(geocode_result)

# g = json.dumps(data[0], indent = 4, sort_keys=True)
# print(g)
# #Googlemaps dagi kiritilgan manzil malumotlarini chiqarib beradi.




# Bular Pythondan JavaScript ga yani jsonga o'tkazganimizda shunday o'zgaradi.

# Python      JavaScript

# dict        Object
# list        Array
# tuple       Array
# str         String
# int         Number 
# float       Number 
# True        true
# False       false
# None        null                
























