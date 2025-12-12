"""
31-dars: Inkapsulyatsiya va klassga oid xususiyat va metodlar.
Created on Tue Oct  7 09:47:14 2025
@author: Sherjahongir
"""

from uuid import uuid4


class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narx,km=0):
        """Avtomabilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1


# uuid dan import uuid4 bu id raqm chiqaradi va hech qachon takrorlanmaydi
#print(uuid4())
#46598cc-9ce0-4250-b48e-47d1c8884742


# Bu yerda km va id oldida __ chiziq bo'lgani uchun ular INKAPSULYATSIYA deyiladi
# va ularga o'zgartirishni faqat yangi def ochib qilish mumkin
# hamda ular ko'rinmaydi

# avto1 = Avto("GM","Malibu","Qora",2020,40000,1000)
# avto1.narx
# Out[58]: 40000

# Bu buyruq bilan ularni ko'rish mumkin yani inkapsulyatsiyani.
# avto1.get_km()
# Out[61]: 1000

    @classmethod
    def get_num_avto(cls):  # cls yani class ni uzatish degani
        return cls.__num_avto
    
    def get_km(self):  # self yani objektni uzatish degani
        return self.__km
    
    def get_id(self):
        return self.__id

    def add_km(self,km):
        """Mashinaning km ga yana km qo'shuvchi metod"""
        if km>=0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")
            
# NATIJASI

# avto1.get_km()
# Out[10]: 1000
# avto1.add_km(2000)
# avto1.get_km()
# Out[12]: 3000
# avto1.add_km(-2000)
# Mashina km kamaytirib bo'lmaydi

avto1 = Avto("GM", "Malibu","Qora",2020,40000,1000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000,30000)
avto3 = Avto("Toyota","Carolle","Silver",2021,30000,25000)
print(Avto.get_num_avto())








#avto1 = Avto("GM","Malibu","Qora",2020,40000,1000)














































