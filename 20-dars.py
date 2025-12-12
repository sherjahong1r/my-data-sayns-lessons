"""
20-dars: FUNKSIYADAN QIYMAT QAYTARISH
Created on Wed Sep 24 06:26:40 2025
@author: Sherjahongir
"""


def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism # o'zgaruvchining qiymatini qaytaradi va qaytarish deb
# tarjima qilinadi. Hamda bu mahalliy o'zgaruvchi deyiladi va faqat shu 
# funksiyaning ichida ishlaydi.
talaba = toliq_ism_yasa('olim', 'olimov')
talaba1 = toliq_ism_yasa('olim', 'hakimov')
talaba2 = toliq_ism_yasa('hakim', 'olimov')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
print(f"{talaba} darsga kechikib keldi")
    
print("\n")

def toliq_ism_yasa(ism, familiya, otasining_ismi=''): # Bu yerda 
# otasining_ismi ga bo'sh joy ochilgani yozsa ham yozmasa ham bo'ladi
     """Toliq ism qaytaruvchi funksiya"""
     if otasining_ismi:
         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
     else:
         toliq_ism = f"{ism} {familiya}"
     return toliq_ism.title()
talaba1 = toliq_ism_yasa('olim','hakimov') 
talaba2 = toliq_ism_yasa('hakim', 'olimov','abrorivich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

print("\n")

def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narx':narxi}
    return avto
avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Yili: {avto['yil']}. Narxi: {narx}")
    
print("\n")

def oraliq(min,max):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar
print(oraliq(0,10))
print(oraliq(10,21))

print("\n")
print("\n")


def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narx':narxi}
    return avto
print("Saytimizda avtolar ro'yxatini shakllantiramiz.")
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
print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()} Yili:"
          f"{avto['yil']}. {korobka} korobka. Narxi: {narx}")
    
    











































































































