# -*- coding: utf-8 -*-
"""
29-dars: Obyektlar bilan ishlash
Created on Fri Oct  3 09:26:03 2025
@author: Sherjahongir
"""

# Talba clasining metodlari yani unga ortiqcha funksiya va o'zgartirishlar 
# kiritayotganda consoleda belgilab o'zgartirish emas balki metodlar bilan 
# yani def lar bilan o'zgartirish tavsiya etiladi.

# Shuningdek o'zgartirishlar uchun set dan va ko'rsatuvchilar uchun get dan
# foydalanish tavsiya etiladi, set_bosqich va get_bosqich kabi.



class Talaba:
    """talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_age(self,yil):
        """talabaning yoshini qaytaradi"""
        return yil - self.tyil
    
    def set_bosqich(self,yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich
# Natijasi set bilan bosqichni o'zgartirish
# talaba1 = Talaba("Alijon","Valiyev",2004)
# talaba1.set_bosqich(2)
# talaba1.get_info()
# Out[59]: 'Alijon Valiyev. 2-bosqich talabasi 
        
    def update_bosqich(self):
        """Talabaning bosqichini 1 taga ko'paytirish"""
        self.bosqich +=1
# Natijasi Bu updete_bosqichga har safar murojat qilganimizda kurs oshib boradi.
# talaba1.update_bosqich()
# talaba1.get_info()
# Out[64]: 'Alijon Valiyev. 4-bosqich talabasi

    def get_info(self):
        """Talabaning malumotlarini pastdagilar asosida qaytaradi"""
        return(f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi")


# YANGI CLASS.


class Fan():
    """Fan nomli class"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_name(self):
        """Fan nomi"""
        return self.nomi
    
    def get_students(self):
        """Fanga yozilgan talabalar haqida malumot"""
        return [talaba.get_info() for talaba in self.talabalar]
        
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni
    
    

matematika = Fan("Oliy matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2002)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

# Natijasi
# matematika.get_students()
# Out[9]: 
# ['Alijon Valiyev. 1-bosqich talabasi',
#  'Hasan Alimov. 1-bosqich talabasi',
#  'Akrom Boriyev. 1-bosqich talabasi']


# dir(Talaba) Bu bizga oynada yozgan deflar ro'yxatini va umuman yozmagan def 
# lar ro'yxatini ham chiqaradi biz yozganlar eng tagida bo'ladi. Bu consoleda.

# Bu pastdagi metod faqat biz yozgan deflar ro'yxatini chiqaradi.
def see_methods(klass):
    return [method for method in dir(klass) if not method.startswith('__')]

# Natijasi
# see_methods(Talaba)
# Out[30]: 
# ['get_age',
#  'get_info',
#  'get_lastname',
#  'get_name',
#  'set_bosqich',
#  'update_bosqich']

# dict bilan consolege pastdagiday murojat qilsak talaba1 ga tegishli xususiyat-
# larni chiqarib beradi.
# talaba1.__dict__
# Out[32]: {'ism': 'Alijon', 'familiya': 'Valiyev', 'tyil': 2000, 'bosqich': 1}

# Agar dictga keys ni ham qo'shsak kalit so'zlarini chiqaradi consolega.
# talaba1.__dict__.keys()
# Out[40]: dict_keys(['ism', 'familiya', 'tyil', 'bosqich'])




































