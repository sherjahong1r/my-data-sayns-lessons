"""
#5-dars: (string) matn bilan ishlash.
#Created on Thu Sep 18 21:18:39 2025
#author: Sherjahongir
"""

matn = "men yangi 🔨 sotib oldim"
smayl = "🤣"
print(matn, smayl)

ism = "Ahmat"
print("mening ismim " + ism)

ism = 'Ahad'
familya = 'Qayum'
print(ism + familya, ism + " " + familya)

ism = "Ahad"
familya = "Qayum"
ism_sharif = f"{ism} {familya}"
print(ism_sharif)

ism = "James"
familya = "Bond"
print(f"salom, mening ismim {familya}, {ism} {familya}!")

print('Hello World')
print('Hello \tWorld')
print('Hello \nWorld')

ism = 'mistr'
familya = 'been'
ism_sharif = f'{ism} {familya}'
print(ism_sharif.upper())
ism_sharif = ism_sharif.upper()
print(ism_sharif.capitalize())
print(ism_sharif.title())
print(ism_sharif.lower())

meva = "    olma    "
print(meva)
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + "ni yaxshi ko'raman")
print("Men " + meva + "yaxshi ko'raman")

ism = input("Ismingiz nima?")
print("Assalomu alaykum, " + ism)

ism = input("Ismingiz nima?\n>>>")
print("Assalomu alaykum, " + ism.title())












