"""
Mavzu: Dunder metodlar (1-qism) and (2-qism) birgalikda.
Created on Tue Oct  7 21:08:49 2025
@author: Sherjahongir
"""

class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx):
        """Avtomabilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        Avto.__num_avto += 1

    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
    
# NATIJALAR:

# avto1.narx
# Out[5]: 40000
# print(avto1)
# Avto: GM Malibu
# repr(avto1)
# Out[9]: 'Avto: GM Malibu'

    
    def __eq__(self,y):  # Bu yerda self x ga teng. == bu tengmi degani.
        return self.yil==y.yil
    
# avto1==avto2
# Out[19]: False
# avto3==avto4
# Out[20]: False

    def  __lt__(self,y):
        return self.narx<y.narx # Bu katta yoki kichikni aniqlaydi narxning.
    
# avto1<avto2
# Out[28]: False
# avto4>avto3
# Out[29]: True

    def __le__(self,y):
        return self.narx<=y.narx  # <=, >= teng yo katta, kichik yo teng degani.
    
# avto1>=avto2
# Out[31]: True
# avto4<=avto3
# Out[32]: False


class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
    
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat): # Bu orqali qiymatni o'zgartirish mumkin
        self.avtolar[index]=qiymat

# Natijasi
# salon1[0]
# Out[4]: Avto: GM Malibu
# salon1[0] = Avto("BMW",'x7',"qora",2020,70000)
# salon1[0]
# Out[11]: Avto: BMW x7
    
    def __call__(self,*qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]  # Bu __call__ bilan salon1()
# natijalarni to'g'ridan to'g'ri chiqaramiz va qolgan avtolarni ham qo'shishimiz
# salon1()
# Out[13]: [Avto: GM Malibu, Avto: GM Lacetti, Avto: Toyota Carolla, Avto: Mazda 6]


# salon1[2]
# Out[41]: Avto: Toyota Carolla
# salon1[:]
# Out[42]: [Avto: GM Malibu, Avto: GM Lacetti, Avto: Toyota Carolla, Avto: Mazda 6]
    
    def __add__(self,y): # Bu bilan 2 ta salon va avtolarni qo'shganmiz
        if isinstance(y,AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {y.name}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon # boshqa_salon ni biz y ga o'zgartirdik.
        elif isinstance(y.Avto):
            self.add_avto(y) # Bu bilan aks holda salonga avto qo'shish ham mumkin
            
    def add_avto(self,*qiymat): # Bu bilan avtolarni qo'shganmiz
        for avto in qiymat:
            if isinstance(avto,Avto): # Bu isinstance malum bir obyekt malum bir 
# klassga tegishlimi yoki yo'qmi shuni tekshiradi True or False deb.
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")
    
    

# Natijasi
#salon1(avto5,avto6)
# salon1()
# Out[44]: 
# [Avto: GM Malibu,
#  Avto: GM Lacetti,
#  Avto: Toyota Carolla,
#  Avto: Mazda 6,
#  Avto: Volkswagen Polo,
#  Avto: Honda Accord]

    
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota","Carolla","Silver",2018, 30000)
salon1.add_avto(avto1,avto2,avto3)

avto4 = Avto("Mazda","6","Qizil",2015,35000)
avto5 = Avto("Volkswagen","Polo","Qora",2015,23000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)
salon2(avto4,avto5,avto6)


# Bu bilan salonlarni bir birga qo'shganmiz def __add__ bilan.
# salon1()
# Out[72]: [Avto: GM Malibu, Avto: GM Lacetti, Avto: Toyota Carolla]
# salon2()
# Out[73]: [Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord]
# 
# Out[80]: 
# [Avto: GM Malibu,
#  Avto: GM Lacetti,
#  Avto: Toyota Carolla,
#  Avto: Mazda 6,
#  Avto: Volkswagen Polo,
#  Avto: Honda Accord]
# salon3.name
# Out[81]: 'MaxAvto Avto Lider'


# __init__() – obyekt yaratilganda ishga tushadi
# __repr__() – obyekt haqida matn ko‘rinishida ma’lumot beradi
# __str__() – print() ishlatilganda qanday chiqish bo‘lishini belgilaydi
# va hokazo.


# Nima uchun ular "ikki pastki chiziq" bilan yoziladi?

# Bu Python protokoli.
# Ya’ni bu nomlar orqali siz til darajasidagi maxsus xatti-harakatni sozlaysiz.

# Masalan:

# Metod nomi	Nimaga javob beradi	Misol
# __init__	Obyekt yaratilganda avtomatik chaqiladi	avto1 = Avto()
# __repr__	repr() yoki print() chaqirilganda obyektni qanday ko‘rsatishni belgilaydi	print(avto1)
# __getitem__	Obyektni ro‘yxat kabi [index] bilan olish	salon1[0]
# __setitem__	Obyektga [index] = qiymat tarzida yozish	salon1[1] = avto2
# __len__	len() funksiyasi ishlaganda	len(salon1)
# __lt__, __le__, __gt__	<, <=, > taqqoslashlarda	avto1 < avto2



























