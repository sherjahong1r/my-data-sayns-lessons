"""
16-dars: NESTING (nesting - ichma-ich degani bunda biz f buyrug'i bilan bir 
nechta buyruqlarni bir qatorga yozishimiz mumkin).
#Created on Mon Sep 22 11:41:48 2025
#author: Sherjahongir
"""


car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':'2018',
        'narx':'13000',
        'km':'50000',
        'karobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':'2015',
        'narx':'9000',
        'km':'89000',
        'karobka':'mexanik'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':'2019',
        'narx':'15000',
        'km':'20000',
        'karobka':'mexanika'
        }

print("\n")

car = car2
print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, {car['narx']}$")
# Bu yerda faqat bittasini chiqarish mumkun 

print("\n")

cars = [car0, car1, car2]
for car in cars:
     print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, {car['narx']}$")
#Bu yerda 3 ta jadvalni ham birdaniga chiqaramiz

print("\n")

print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")
# Bu ko'd bilan biz carsning ichidagi natijalarni chiqarishimiz mumkin.

print("\n")

malibus=[]
for n in range(10):
    new_car = {
        'model':'malibu',
        'range':None,
        'yil':2020,
        'narx':None,
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)
#Bu yerda 10 ta rusumi bir xil bo'lga malibuni chiqardik range bilan.



for malibu in malibus[:3]:
    malibu['rang']='qizil'   

for malibu in malibus[3:6]:
    malibu['rang']='qora'
    
for malibu in malibus[6:]:
    malibu['range']='qora'
    malibu['korobka']='mexanika'  
    
for malibu in malibus:
     if malibu['korobka']=='avto':
         malibu['narh']=40000
     else:
         malibu['narh']=35000
    
for malibu in malibus:
    print(malibu)
# Hamda yuqoridagi jadvalga o'zgartirishlar kiridik.

print("\n")

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi")
    for til in tillar:
        print(f'{til.upper()} ', end=' ') 
#Bu yerda f bilan end joy tashlanmasligini taminlaydi 
#agar u bo'lmaganida joy tashlab yozardi.

print("\n")

hamkasblar = {
    'ali':{'familya':'valiyev',
          'tyil':1995,
          'malumot':'oliy',
          'tillar':['python', 'c++']
           },
    'vali':{'familya':'aliyev',
           'tyil':2001,
           'malumot':"o'rta-maxsus",
           'tillar':['html', 'css', 'js']},
    'hasan':{'familya':'husanov',
            'tyil':1999,
            'malumot':'maxsus',
            'tillar':['python', 'php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan, "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
        
# Bu yerda info va ism o'rnini boshqa bir hil bo'lgan nom bilan atasak 
#ham bo'ladi

































