"""
#8-dars: Ro'yxat bilan ishlash. O'zgarmas ro'yxatlar(Tuples)
#Created on Fri Sep 19 23:25:22 2025
#author: Sherjahongir
"""


cars = ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']

sonlar = [3, 2, -1, 4, 28, 234]

narxlar = [12000, 22500, 45678, 26000, 23000, 10000]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print("Eng arzon narx:", arzon,", Eng qimmat:", qimmat,", jami: ", jami)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

# TUPLES bunda o'zgarish kiritib bo'lmaydi chunki bu oddiy qavsda
# bo'ladi ('bus', 'car', 'bear') 
# LIST bunga o'zgarish kiritsa bo'ladi chunki ['bus', 'car'] qavs bo'ladi. 




#Bunda sort buyrug'i alifbe tartibi bo'yicha joylashtiradi.
#cars
#Out[83]: ['bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#cars.sort()
#print(cars)
#['audi', 'bmw', 'daevo', 'mercedes benz', 'tesla', 'volvo']

#Agar orasida katta harf ham bo'lsa birinch katta harfni joylashtiradi
#keyin alifbe tartibida davom etadi.
#Out[87]: ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#cars.sort()
#print(cars)
#['Bmw', 'audi', 'daevo', 'mercedes benz', 'tesla', 'volvo']

#Bunda sortga reverse buyrug'ini qo'shsak teskari tartib bilan joylashadi.
#cars.sort(reverse=True)
#cars
#Out[92]: ['volvo', 'tesla', 'mercedes benz', 'daevo', 'audi', 'Bmw']

#Bunda sorted buyrug'i orqali asl ro'yxatga tegmagan holda tartiblaymiz,
#huddi shu buyruqlarni sonlarga nisbatan qo'lashimiz ham mumkin.
#cars
#Out[95]: ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#print(sorted(cars))
#['Bmw', 'audi', 'daevo', 'mercedes benz', 'tesla', 'volvo']
#cars
#Out[97]: ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#print(sorted(cars, reverse=True))
#['volvo', 'tesla', 'mercedes benz', 'daevo', 'audi', 'Bmw']
#sonlar
#Out[102]: [3, 2, -1, 4, 28, 234]
#sonlar.sort()
#print(sonlar)
#[-1, 2, 3, 4, 28, 234]

#Bunda soni nechtaligini aniqlashimiz mumkin len yani lengiz uzunlik bilan.
#cars
#Out[106]: ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#len(cars)
#Out[107]: 6

#Bunda esa uzunlik degan jadval ochishimiz va atributlar nechtaligini ko'ramiz
#bu jadvalda ko'rinadi.
#sonlar
#Out[108]: [3, 2, -1, 4, 28, 234]
#uzunlik = len(sonlar)
# uzunlik
# Out[4]: 6

#Bunda range orqali sonlar jadvalini tashkil qilamiz va 0,10 gacha qilsak
# 0 dan 9 gacha chiqarib beradi. 
#sonlar = list(range(0,10))
#sonlar
#Out[20]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#list(range(21,30))
#Out[22]: [21, 22, 23, 24, 25, 26, 27, 28, 29]

#Bunda range bilan 1 dan 20 gacha sonlarning 2 qadam tashlab chiqar degani.
#toq_sonlar = list(range(1,20,2))
#toq_sonlar
#Out[26]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#juft_sonlar = list(range(0,20,2))
#juft_sonlar
#Out[30]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#sonlar = list(range(0,100,10))
#sonlar
#Out[33]: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#Bunda orasidan eng maxsimum va minimum hamda umumiy yig'indisini
#topshimiz mumkin sum bilan.
#narxlar
#Out[36]: [12000, 22500, 45678, 26000, 23000, 10000]
#min(narxlar)
#Out[37]: 10000
#max(narxlar)
#Out[38]: 45678
#sum(narxlar)
#Out[39]: 139178

#Bunda biz ro'txatdan oralig'idagi hohlaganimizni chiqarib olamiz.
#cars
#Out[55]: ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#print(cars[2:5])
#['volvo', 'audi', 'tesla']
#Bunda birdan boshlab oxirigacha oladi, yoki [:5] bunda 0 dan 5 gacha oladi.
#print(cars[1:])
#['mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']

#Bu orqali biz nusxalashimiz va boshqa buyruqlar kiritishimiz mumkin
#lekin bunda bir buyruq har ikkisiga ham tasir qiladi.
#cars
#Out[61]: ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#my_cars = cars
#print(cars)
#['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#print(my_cars)
#['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#my_cars.remove('mercedes benz')
#my_cars[0] = "daevo"
#print(my_cars)
#['daevo', 'volvo', 'audi', 'tesla', 'daevo']
#cars
#Out[68]: ['daevo', 'volvo', 'audi', 'tesla', 'daevo']

#Bunda nusxalaganimiz biriga o'zgartirish kiritsak boshqasiga tasiri yo'q.
#cars
#Out[75]: ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#my_cars = cars[:] # chunki bu yerda [:] bu belgi bor.
#my_cars
#Out[77]: ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#my_cars.remove('Bmw')
#my_cars
#Out[79]: ['mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']
#cars
#Out[80]: ['Bmw', 'mercedes benz', 'volvo', 'audi', 'tesla', 'daevo']



























