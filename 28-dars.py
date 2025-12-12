# -*- coding: utf-8 -*-
"""
28-dars: (klasslar) Object oriented Dasturlash. klass va obyekt
Created on Fri Oct  3 08:12:18 2025
@author: Sherjahongir
"""


# Biz shu vaqtgacha qilgan dasturlar masalan (son topish o'yini) chiziqli
# dasturlashga misol bo'ladi.

# word va shu kabi exel dasturlari object oriented dasturlash tamoyiliga
# misol bo'ladi. 

# Classlar bilan funksiya tuzish.

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_age(self,yil):
        return yil - self.tyil
    
    def tanishtir(self):
        return(f"Ismim {self.ism} {self.familiya}, Tug'ilgan yilim {self.tyil}")
# Biz bu yerda return o'rniga printdan ham foydalansak bo'ladi ammo print faqat
# natijani consoleda chiqaradi, returnda esa matnni web dastur va interface 
# larda ham chiqarish ham mumkin.       
    
talaba1 = Talaba("Olim","Olimov",2000)
talaba2 = Talaba("Hasan","Asadov",2003)
talaba3 = Talaba("Akmal","Abrorov",2001)


# NATIJALARI:
    
# talaba2.ism
# Out[5]: 'Hasan'
# talaba1.familiya
# Out[6]: 'Olimov'
# talaba3.tyil
# Out[7]: 2001

# talaba2.get_name()
# Out[12]: 'Hasan'

# talaba1.get_lastname()
# Out[16]: 'Olimov'

# talaba2.get_age(2025)
# Out[14]: 22

# talaba3.tanishtir()
# Ismim Akmal Abrorov, Tug'ilgan yilim 2001





# O'zim yasaga class!!


class Telefonlar:
    def __init__(self,rusm,rang,yil):
        self.rusm = rusm
        self.rang = rang
        self.yil = yil

    
    def tel_rusumi(self):
        return self.rusm
    
    def what_color(self):
        return self.rang
    
    def when_in(self):
        return self.yil
    
    def korsatma(self):
        return(f"Telefon modeli {self.rusm}, uning rangi {self.rang},"
               f"va {self.yil}-yilda chiqqan")


telefon1 = Telefonlar("Iphone","ko'k",2025)
telefon2 = Telefonlar("Samsung","qora",2023)
telefon3 = Telefonlar("Dous","qora",2015)


# NATIJASI:

# telefon1.korsatma()
# Out[8]: "Telefon modeli Iphone, uning rangi ko'k, va 2025-yilda chiqqan"
# telefon2.korsatma()
# Out[10]: 'Telefon modeli Samsung, uning rangi qora, va 2023-yilda chiqqan'









































