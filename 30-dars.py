# -*- coding: utf-8 -*-
"""
30-dars: VORISLIK VA POLIMORFIZM
Created on Mon Oct  6 22:55:49 2025
@author: Sherjahongir
"""

# Shaxs clasini pastdagi Talaba clasiga ulashimiz bu VORISLIK deyiladi.
# hamda talaba clasini ham pastdan yana bir clasga vorislik clas qilishimiz 
# mumkin
# Shaxda mavjud bo'lgan get_infoga talaba clasida yana o'zgartirish kiritsak
# POLIMORFIZM deyiladi.



class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan "
        return info
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    


class Talaba(Shaxs): # Shaxs bu yerda super class deyiladi, Talaba esa voris 
# class deyiladi. Hamda Talaba clasiga Shaxs clasida bo'lgan get_info va get_age
# ham meros bo'lib o'tadi Shaxs super class bo'lgani uchun. Hamda har doim 
# super class keyin voris class keladi aks holda xatolik bo'ladi.
    """Talaba klasi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida malumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
# Bu get_info yuqoridagi Shaxs classida ham bor edi, ammo u malumotlarga yana 
# malumot qo'shish uchun talabada da ham get_info ni yaradik bu holatga 
# POLIMORFIZM deyiladi.

# NATIJASI CONSOLEDAGI

# Bu malumotlar shaxs classidan olingan
# talaba1 = Talaba("Alijon","Valiyev","FF1234567",2001,"N00011")
# talaba1.get_info()
# Out[27]: "Alijon Valiyev. Passport:FF1234567, 2001-yilda tug'ilgan "
# talaba1.get_age(2025)
# Out[28]: 24

# Bu malumotlar yanigi Talaba clasida yaratilgan get_info dan olingan
# talaba1 = Talaba("Alijon","Valiyev","FF1234567",2001,"N00011")
# talaba1.get_info()
# Out[43]: 'Alijon Valiyev. 1-bosqich. ID raqami: N00011'


# Hamda Talaba va shaxs ga yangi qiymat manzil degan yangi classni ni kiritamiz

class manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
talaba1_manzil = manzil(12, "Olmazor", "Bo'g'bon","Samarqand")
talaba1 = Talaba("Alijon","Valiyev","FF1234567",2001,"N00011",talaba1_manzil)
# Bunda hammasini bittaga yozsak ham bo'lardi ammo talaba1_manzil deganga 
# alohida yozib olib pastdagining davomiga o'sha talaba1_manzil deb davom etirdik


# NATIJASI
# talaba1.manzil.get_manzil()
# Out[47]: "Samarqand viloyati, Bo'g'bon tumani, Olmazor ko'chasi, 12-uy"

# Bunda talaba1 ning ichidagi manzil va uning ham ichidagi get_manzil()
# ga murojat qildik va ularni nuqta bilan ajratib murojat qilish kerak.

















