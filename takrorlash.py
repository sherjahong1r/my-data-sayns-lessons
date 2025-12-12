"""
Created on Fri Nov  7 21:27:42 2025
Team: Strengthening (Mustahkamlash)
@author: Sherjahongir and Mosh
"""

print("\n")

# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)
# Ballandlik kiritilsa og'rlikni o'lchab beradi.

print("\n")

name = 'Jennifer'
print(name[1:-1]) # Bu shu raqamlar oralig'idagi harflarni ko'rsatadi
print(name.find('n')) # Bu shu harf nechinchi tartibda ekanini ko'rsatadi

print("\n")

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder' # bu ham bir usuli 
print(message)
msg = f'{first} [{last}] is a coder' # qulay usul
print(msg)

print("\n")

course = 'Python for Beginners'
print(len(course))  # nechta joy ketganini aniqlaydi
print('Python' in course) # Python so'zi yuqoridagi jumlada bormi degani.
print('python' in course) # python so'zi yuqoridagi jumlada bormi degani.
print(course.upper()) # Hammsi katta
print(course.title()) # Hamma so'zning boshi katta
print(course.capitalize()) # Bosh harf katta qolgani kichkina
print(course.lower()) # hammasi kichkina 
print(course.casefold()) 
print(course.encode())

print("\n")

print(10 - 3)
print(10 + 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3) # nechchi qoldiq qolganini ko'rsatadi
print(10 ** 3) # Darajasini ko'rsatadi 10 ning 3 darajasi 1000 ga teng.
print("\n")

x = 10
x -= 3 # Yoki += qilsak ham bo'ladi va qo'shib ko'rsatadi
print(x)

print("\n")
x = 10 + 3 * 2 ** 2
print(x)

print("\n")
x = 2.7
print(round(x)) # Bu round yaxlitlab oladi

print("\n")
x = 2.9
print(abs(-2.9)) # Bu oldidagi ishorasini olib tashlaydi.


print("\n")

import math # math ni import qilib olib keldik

print(math.floor(2.9)) # bu pastga yaxlitlaydi
print(math.ceil(2.1))  # bu esa yuqoriga yaxlitlaydi


print("\n")

savol = input("When is weather Today:\n "
              "qanday kunligini bilmasangiz istagan harf yo son kiriting\n"
              "(hot/cold) \n>>>")


if savol == "hot":
    print("It's a hot day")
    print("Drink plently of water")
elif savol == "cold":
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")
































