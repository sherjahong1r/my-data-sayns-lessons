"""
38-dars: Python Standart kutubxonasi
Created on Mon Oct 20 09:42:55 2025
@author: Sherjahongir
"""


# tashqi yoki ichi kutubxona degani boshqa bir dasturchilar tomonidan
# yozilgan turli xil tayyor funksiyalar, modullar va paketlarni yig'indisi.




import datetime as dt

# datetime()
hozir = dt.datetime.now()
print(hozir)
# # # Sanani ajratib olish
print(hozir.date())
# # # Vaqtni ajratib olish
print(hozir.time())
# # # Soatni ajratib olish
print(hozir.hour)
# # # Minutni ajratib olish
print(hozir.minute)
# # # Sekundni ajratib olish
print(hozir.second)

# NATIJASI
# 2025-10-20 10:06:37.591002
# 2025-10-20
# 10:06:37.591002
# 10
# 6
# 37

# YOKI CONSOLEGA BUNDAY YOZAMIZ
# hozir.hour
# Out[59]: 9
# hozir.minute
# Out[60]: 56
# hozir.second
# Out[61]: 11

print("\n")




# date()
bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")

# Kechagi sana bu aniq vaqt
kecha = bugun - dt.timedelta(days=1)
print(f"Kechagi sana: {kecha}")

kecha = dt.date(2025, 10, 19)
print(f"Kecha sana: {kecha}")

ertaga = dt.date(2025, 10, 23)
print(f"Ertangi sana: {ertaga}")
farqi = ertaga-bugun
print(f"Ertan kelishiga {farqi} soat qoldi")

# NATIJASI

# Bugungi sana: 2025-10-20
# Kecha sana: 2025-10-19
# Ertangi sana: 2025-10-21
# Ertan kelishiga 2 days, 0:00:00 soat qoldi

print("\n")


# time()
hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")

vaqtKeyin = dt.time(12,30,55)
print(f"biroz vaqtdan so'ng: {vaqtKeyin}")
print("Shuning uchun tezroq o'qi")

# NATIJASI

# Hozir soat: 10:25:40.793624
# biroz vaqtdan so'ng: 12:30:55
# Shuning uchun tezroq o'qi


print("\n")



# Sanalar orasidagi farq
bugun = dt.date.today()
ramazon = dt.date(2025, 11, 23)
farq = ramazon-bugun
print(f"Ramazonga {farq.days} kun qoldi")

# Ramazonga 34 kun qoldi


print("\n")


# Soatlar orasidagi farq
hozir = dt.datetime.now()
kino = dt.datetime(2025, 10, 21, 23, 45, 00)
farq = kino-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Kino boshlanishiga {farq.days} kunu {soatlar} soat qoldi")
     

print("\n")


import math

PI = math.pi
print(f"PI ning qiymati: {PI}")
E = math.e  # e bu matematikada natural logarifmlarning asosi hisoblanadi.
print(f"e ning qiymati: {E}")

# # Trigonometriya
math.sin(math.pi/2)
math.cos(0)
math.tan(PI)
print()

# # radianlar va burchaklar o'rtasidagi konvertasiya
print(math.degrees(math.pi/2)) # degrees degani radian qiymatni
# bersak burchak qiymatni qaytaradi
print(math.radians(90))  # Bunda aksincha burchak qiymatda bersak radianda 
# qaytaradi

# # logarifmlar
# natural logarifm
math.log(5)
# 10 asosli logarifm
math.log10(100)

# NATIJASI CONSOLEDAGI

# math.log10(100) # Buning manosi log10 ning pastidagi 2 yani kvadrati 100 ga
# Out[11]: 2.0  # teng degani pastdagi ammallar ham huddi shu tartibda qilinadi
# math.log(5)
# Out[12]: 1.6094379124341003
# math.log10(5)
# Out[13]: 0.6989700043360189
# math.log2(4)
# Out[14]: 2.0


# # Sonlarni yaxlitlash
x= 4.6
print(math.ceil(x)) # ceil - tom degani yani yuqoridagi songa yaxlitlaydi
print(math.floor(x)) # floor - pol degani yani pastdagi songa yaxlitlaydi

# NATIJASI
# 5
# 4
# round(x)
# Out[17]: 5 # consolega bunday round deb yozsak eng yaqin songa yaxlitlaydi.


# # Kvadrat ildiz
x=81
math.sqrt(x)

# math.sqrt(81)
# Out[19]: 9.0
# math.sqrt(123456787654) 
# Out[20]: 351364.1809490546


# Darajaga oshirish
math.pow(x,3)  # x ning kubi
math.pow(x,5)  # x ning 5- darajasi
math.pow(x,1/3)  # x dan kub ildiz

# math.pow(x,3) # 81 ning kubi
# Out[22]: 531441.0


print("\n")


from pprint import pprint
import json

filename = 'bemor.json.py'
with open(filename) as f:
    bemor = json.load(f)
    
pprint(bemor) # Bunga print ning o'zini yozsak ham bo'lardi ammo pprint 
# # bu tartibli va chiroyli qilib chiqaradi kod natijasini consolega.
# # print ning o'zi esa bir chekadan chiqaradi pprint esa kalit va natijalari
# # bilan chiqaradi.

print('\n')

import requests
r = requests.get('https://api.github.com')

pprint(r.json())


print('\n')

# RegEx = Regular Expressions deyiladi - andozalar yani matnlarni izlash uchun
# andoza yaratadi.

import re 
from words import words

word1 = "mемuр"
word2 = "mомuр"
word3 = "mулпор"

#andoza = "^m...р$"  # ^ bu boshlanishi m dan va 3 ta harfdan keyin p bilan 
# tugashlini $ bu belgi anglatadi boshlanishi esa ^ bu.

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

andoza = "^а...д$" # bunda agar andozadagidek bo'lgan shunday so'zlarni words
matches = []       # ichidan topib chiqar degani
for word in words:
    if re.match(andoza,word):
        matches.append(word)
        
print(matches)

# NATIJASI
#['абжад', 'авлод', 'аврод', 'аждод', 'ақоид']



print("\n")


# # Emailni ajratib olish
matn = """Maqolalar 2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida
Quyidagi yo'nalishdagi maqolalar qabul qilinadi: Sher_Jahongir@gmail.com
    Aniq va tabiiy fanlarni zamonaviy pedagogik texnalogiyalar asosida o'qitish metodikasi.
    Umumta'lim fanlarni o'qitishda STEAM yondashuvining o'rni va ahamiyati. """
    
andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(email)

print("\n")


# # Kuchli parolni tekshirish
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harfi, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi bolishi kerak): '

while True:
    password = input(msg) # yuqoridagi msg talablarni input bilan chiqaradi
    if re.match(andoza,password): # Bu yerda match bilan tekshiradi kiritilgan 
        print("Maxfiy so'z qabul qilindi") # password andozaga to'g'ri kelishini
        break
    else:
        print("Maxfiy so'z talabga javob bermaydi")

# NATIJASI
# Yangi parol kiriting(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harfi,
# 1 ta kichik harf, 1 ta son va 1 ta maxsus belgi bolishi kerak): jahongir
# Maxfiy so'z talabga javob bermaydi
# Yangi parol kiriting(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harfi,
# 1 ta kichik harf, 1 ta son va 1 ta maxsus belgi bolishi kerak): Jahongir_$00
# Maxfiy so'z qabul qilindi






# й ц у к е н г ш щ з х ъ  \
# ф ы в а п р о л д ж э 
# я ч с м и т ь б ю . 




























