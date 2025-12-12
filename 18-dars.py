"""
#18-dars: WHILE RO'YXATLAR VA LUG'ATLAR.
Created on Tue Sep 23 08:06:28 2025
@author: Sherjahongir
"""

print("Yaqin do'slaringiz ro'yxatini tuzamiz.")
ismlar = []
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
    n+=1
    if takrorlash != 'ha':
        break
    
print("Do'slaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())

print("\n")

dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q": #Yani yo'q degandan keyin ishora yordamida to'xtatamiz
    # va pastdagi buyruqlarni tekshirishga o'tadi.
        ishora = False 
        
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")

print("\n")

cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia', 'lacetti']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)    

# Bu yerda while ichida remove bilan nexia ning hammasini o'chirish mumkin
# Agarda while bo'lmaganda faqatgina bitasini o'chirardi.

print("\n")

talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop() # pop bilan oxiridan boshlab ismlarni oladi.
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)
    
# Natijasi
#Botirning bahosini kiriting: 3
#Botir baholandi
#Olimning bahosini kiriting: 1
#Olim baholandi
#Husanning bahosini kiriting: 2
#Husan baholandi
#Hasanning bahosini kiriting: 3
#Hasan baholandi

#print(talabalar)
#[]

#baholangan_talabalar
#Out[9]: {'botir': 3, 'olim': 1, 'husan': 2, 'hasan': 3}



























































