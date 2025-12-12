"""
40-dars: So'ngi so'z va JUMBOQ
Created on Thu Oct 23 11:14:26 2025
@author: Sherjahongir
"""

#  Xulosa va shu vaqtgacha ko'rilgan darslar tahlili
#  Barcha darslarni takrorlab sodda bo'lsa ham dasturlar tuzish kerak.




###   41-DARS  (JUMBOQ)
import random
n=100
numbers = list(range(1,n+1))
x=numbers.pop(random.randint(1,n+1))
print(x)
# x ni topish
# Yuqorida 1 dan 100 gacha sonlar ichidan tasodifiy bir son tushib qoldi
# hamda o'sha son qaysi ekanligini topishning eng optimal usuli qaysi ekanini
# ko'rsatish usullari.


# 1-usul lekin bu xotiradan katta joy egallar ekan
numbers2 = list(range(1,n+1))
print(sum(numbers2)-sum(numbers))


# 2-usul bu birinchi usulga nisbatan yaxshi chunki oraliqdagi sonlarni xotiraga
# joylamaydi lekin bu ham optimal yechim emas
for i in range(1,n):
    if i not in numbers:
        print(i)
        break
    

#  3-usul eng optimal yechim
summa = n*(n+1)/2  # Bu 1 dan 100 gacha sonlarning yig'indisini hisoblaydigan
print(summa - sum(numbers))   # matematik formula
# 100 x 101 : 2  # Bu 1 dan yuzgacha sonlar yig'indisini hisoblaydi.


















































