"""
17-dars: INPUT() va While tsikli
Created on Mon Sep 22 21:51:46 2025
@author: Sherjahongir
"""
#Input bu qanday qiymat kiritilmasin doim string sifatida qaytaradi
# va uni biz int or float ko'rinishiga o'zgartirishimiz kerak.

# while tsikili berilgan shart to'g'ri (True) bo'lguncha kodni qayta bajaradi
# Shart yolg'on (False) bo'lganda tsikl to'xtaydi.





ism = input("Ismingiz nima?")
savol = f"Salom, {ism.title()}. Yoshingiz nechida?"
yosh = input(savol)
yosh = int(yosh)
#Bu yerda str yani matn ko'rinishidan int sonli ko'rinishga o'tkazib oldik
height = input("Bo'yingiz necha metr? ")
height = float(height)
#Bu yerda o'nli ko'rinishga o'tkazdik height ning o'zini.

print("\n")

son = 1
while son<=25: #toki son 25 dan kichik yoki teng ekan...
     print(son, end=' ') # son ni konsolga chiqaramiz
     son = son + 1 # yoki son += 1 ham shu qiymatga teng hisoblanadi
print(' Dastur tugadi')
#while ning tarjimasi toki degani
# Bu yeda toki 25 ga yetmaguncha sana degani.

print("\n")

## tekshirish yordamida to'xtatish
print("Kiritilgan sonning kvadratini qayturuvchi dastur.")
savol = "Istalgan son kiriting "
savol +="(dastur tugashi uchun exit deb yozing)"
qiymat =''
while qiymat != 'exit': # =! qiymat exit ga teng bo'lamsa degani.
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print(' Dastur tugadi')

print("\n")

## ishora yordamida to'xtatish 
print("Kiritilgan sonning kvadratini qayturuvchi boshqa ikkinchi dastur.")
savol = "Istalgan son kiriting "
savol +="(dastur tugashi uchun exit deb yozing)"
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
print(' Dastur to\'xtadi')
# Bu yana bir usuli yuqoridagi bilan bir xil vazifa bajaradi

print("\n")

print("Kiritilgan sonning kvadratini qayturuvchi uchinchi dastur.")
savol = "Istalgan son kiriting "
savol +="(dastur tugashi uchun exit deb yozing)"
while True: # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break #tsiklni to'xtatish
    else:
        print(float(qiymat)**2)
print(' Dastur end!')


sonlar = list(range(1,11))
for son in sonlar:
    if son == 10:
        break # Bu yerda continue qilsak ham bo'ladi va oxirgi amalni 
        #bajarmay yana boshiga o'tib ketadi
    print(f"{son} ning kvadrati {son**2} ga teng")

print("\n")

son = 0
while son<10:
    son += 1
    if son%2==0:# %2 yordamida sonning qoldig'ini tekshiramiz va umumiy
    # shart yordamida juft son yoki toq son ekanini tekshiramiz
        continue
    else:
        print(son)

#Shuningdek abadiy tsikllar ham bor yani ko'dlar umuman to'tamaydi misol
# uchun yuqoridagi misolda son += 1 qatori yo'q bo'lsa yoki paski qatorlarda 
# joylashib qolsa ro'y beradi. Bunday holda consolda yuqori o'ng burchagida 
# tugmani qizil qilib belgilaymiz yoki ctrl + c tugmasini bosak to'xtaydi.

son = 1
while son<0:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)
# Bu xato bo'lib abadiy tsiklga misol aslida esa son>0 emas balki son<o
# bo'lishi kerak edi.


























































































