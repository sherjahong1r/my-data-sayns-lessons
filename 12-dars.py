"""
#12-dars: Eng ko'p uchraydigan xatolar.
#Created on Sun Sep 21 10:00:49 2025
#author: Sherjahongir
"""



print("Hello world")  # Eng ko'p uchraydigan xatolar printdan so'ng 
#qavs va qo'shtirnoqqa etibor berish kerak. Hamda consolda hatoni chiqaradi 
# va qatorini ham aytadi. Agar tarjimasini bilmagan holda google transletdan
# foydalanish.
               
print("O'ngacha sanaymiz")
for n in range(10):
     print(n+1)
#Bu yerda pastdagi print for atributi ichida bo'lgani uchun joy tashlanishi 
#kerak kamida bitta. Va har doim Tab + Space dan foydalanaman.
#Hamda joyni har doim bir xil tashlashimiz kerak

son = input("Istalgan son kiriting:")
son = int(son)
print(f"{son} ning kvadrati {son**2} ga teng")
# Bu yerda Type ga etibor berishimiz kerak agar int o'rniga str or float va
#boshqasini qo'ysak ko'd bajarilmaydi.


#Hamda imlo hatolariga etibor berilishi kerak

#Hamda str, int, float typga katta etibor berishimiz kerak.

#Hamda sanoqlar har doim 0 dan boshlanadi, agar 3 ta narsa bo'lsa 
#oxirgisi tartib bo'yicha 2 - raqamda joylashadi.

# pi ning qiymati o'zgarmas 3.14 bu formula, lekin buni pythonga farqi yo'q.

print("\n")

radius = 5
pi = 3.14
aylana_yuzi = pi*radius**2
print(aylana_yuzi)

son = float(input("Istalgan son kiriting uning ildizini aniqlayman:"))
ildiz = son**(1/2) #Bu orqali sonning ildizini aniqlaymiz
print(f"{son} ning ildizi {ildiz} ga teng")















