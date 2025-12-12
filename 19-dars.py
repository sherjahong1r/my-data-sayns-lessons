"""
19-dars: FUNCTIONS (FUNKSIYALAR)
Created on Tue Sep 23 10:02:54 2025
@author: Sherjahongir
"""


# Funksiya bu buyruq bo'lib uni def bilan yaratsa bo'ladi va print() kabi
# ishlaydi pastdagi ko'd buning namunasi va salom_ber degan buyruq yaratildi.



def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum")
    
salom_ber()

# Natija
#Assalomu alaykum
#salom_ber()
#Assalomu alaykum

print("\n")

def salom_ber(ism): # Funksiyani yaratganda foydalanuvchidan qabul qilib
# olayotgan qiymatlar parametr deyiladi, bu yerda ism parametr.
    """Foydalanuvchi ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
salom_ber('hasan')
salom_ber('olim')  # Foydalanuvchi tomonidan funksiyaga uzatilgan qiymatlar 
# argument deb nomlanadi bu yerda hasan va olim argument.

print("\n")

def toliq_ism(ism, familya):
    """Foydalanuvchi ism va familyasini jamlab chiqaruvhi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familyasi: {familya.title()}")

toliq_ism('olim', 'hakimov')
toliq_ism('aliyev', 'vali')

# Shuningdek familya va ismning joyini adashtirmaslik kerak chunki bu hatolik
# bo'ladi va hatolikga olib keladi, boshqa vaziyatlar uchun ham.
# yuqoridagi aliyev vali buning misoli.

print("\n")

def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dasur"""
    print(f"{ism.title()} {2025-tugilgan_yil} yoshda")

yosh_hisobla('ali',2003)

# Buning oldini olish uchun birdaniga yozib ketsak yani natijasini bersak 
# bunday muammo bo'lmaydi pasdagi buning misoli.

yosh_hisobla(ism='olim', tugilgan_yil=1998)




