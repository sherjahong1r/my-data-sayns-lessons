"""
# 11-dars: if-elif-else
#Created on Sun Sep 21 00:35:14 2025
#author: Sherjahongir
#Web sahifa: https://python.sariq.dev
"""



yosh = int(input('Yoshingiz nechida?'))
if yosh<=4:
#    print('Sizga kirish bepul.')
     narx = 0
elif yosh<=12:
#    print('Sizga kirish 5000 so\'m')
     narx = 5000
elif yosh<=18:
#    print("Sizga kirish 8000 so'm")
     narx = 8000
else:
#    print('Sizga kirish 10000 so\'m')
     narx = 10000
print(f"Sizga kirish {narx} so'm")

print("\n")

kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni ekan uff.')
    
print("\n")

kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
   print("Cho'milgani ketdik!")
elif (kun.lower()=='yakshanba' or kun.lower()=='shanba')  and harorat<30:
 print("Uyda dam olamiz")    
    
print("\n")
    
print("Mijoz ovqatlandi")
narx = 15000 # mijoz 15000 so'mga taom oldi
choy = False # mijoz choy olmadi
salat = True # mijoz salat oldi
if choy and salat: #choy ham salat ham olgan bo'lsa
 narx = narx + 10000# narxga 10000 so'm qo'shamiz
elif choy or salat: # agar choy yoki salad olgan bo'lsa
 narx = narx + 5000 # narxga 5000 so'm qo'shamiz
 print(f"Jami {narx} so'm") # yakuniy narxni chiqaramiz
 
print("\n")   
 
narx = 15000 # mijoz 15000 so'mga ovqat oldi
choy = True
salat = False
non = True 
kompot = False
assorti = True # Bularning o'rniga 1 or 0 qo'ysak ham bo'ladi
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
 
if choy: # agar choy olsa
  print("Mijoz choy oldi.")
  narx = narx + 3000
  
if salat: # agar salat olsa
 print("Mijoz salat oldi.")
 narx = narx + 5000
   
if non: # agar non olsa
 print("Mijoz non oldi.")
 narx = narx + 2000
    
if kompot: # agar kompot olsa
 print("Mijoz kompot oldi.")
 narx = narx + 5000
     
if assorti: # agar assorti olsa
 print("Mijoz assorti oldi.")
 narx = narx + 15000
 print(f"Umumiy xarajatlar: {narx} so'm")
 
print("\n")
 
menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
'manti' in menu # Bu yerda menuda manti bormi degani 
#in shunda ichida bormi degan manoni anglatadi.

# Natija
#'manti' in menu
#Out[11]: False
#'osh' in menu
#Out[12]: True

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input("Nima ovqat yeysiz?>>>")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi")
else:
    print("Afsuski bizda bunday ovqat yo'q")
    
# Natija
#menu
#Out[22]: ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
#"sho'rva" not in menu
#Out[23]: True
#"osh" not in menu
#Out[25]: False

#menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
#buyurtmalar = ["osh", "somsa", "manti", "shashlik"]
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    