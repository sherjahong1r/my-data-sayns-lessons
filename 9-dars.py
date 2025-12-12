"""
#9-dars: For tsikili bilan tanishamiz. (FOR LOOP)
#Created on Sat Sep 20 09:23:35 2025
#author: Sherjahongir
"""


mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for belgi in mehmonlar:
    print("Salom", belgi)
    print("Xayr", belgi) #Barchasi mana shunday masofada yoziladi.

#mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
#for mehmon in mehmonlar:
#    print("Salom", mehmon)
    
    
mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
        print(f"Hurmatli {mehmon}, sizni 23 Yanvar kuni bazmga taklif etamiz")
        print("Hurmat bilan, Sherjahongir Tursunmurodov\n")

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

sonlar = list(range(11))
sonlar_kvadrati =[]
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)

dostlar = [] #bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting:"))
print(dostlar)

#5 ta eng yaqin do'stingiz kim?
#1-do'stingizning ismini kiriting:to'rabek
#2-do'stingizning ismini kiriting:shokir
#3-do'stingizning ismini kiriting:dilmurod
#4-do'stingizning ismini kiriting:suhrob
#5-do'stingizning ismini kiriting:farrux
#["to'rabek", 'shokir', 'dilmurod', 'suhrob', 'farrux']


















