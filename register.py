# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18:
#     print("Xush kelibsiz!")
# else:
#     print('Kirish mumkin emas!')



# print("\n")

# login = input("Yangi login tanlang:")
# if len(login)<=5: # 5 harfdan ko'proq bo'lishi kerak
#     print("Login 5 harfdan ko'proq bo'lishi shart")
# else:
#     print("siz to'g'ri kiritingiz")



#     avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']

# for avto in avtolar: #avtolar ichidagi har bir avto uchun
#     if avto == 'bmw':#agar avto bmw ga teng bo'lsa
#         print(avto.upper()) #avto nomini hamma harfini kattalashtir
#     else: #aks holda
#         print(avto.title()) #avto nomi faqat birinchi harfi katta bo'lsin

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni ekan uff.')
    
# print("\n")


# print("Mijoz ovqatlandi")
# narx = 15000 # mijoz 15000 so'mga taom oldi
# choy = False # mijoz choy olmadi
# salat = True # mijoz salat oldi
# if choy and salat: #choy ham salat ham olgan bo'lsa
#  narx = narx + 10000# narxga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salad olgan bo'lsa
#  narx = narx + 5000 # narxga 5000 so'm qo'shamiz
#  print(f"Jami {narx} so'm") # yakuniy narxni chiqaramiz
 


#  print("\n")   
 
# narx = 15000 # mijoz 15000 so'mga ovqat oldi
# choy = True
# salat = False
# non = True 
# kompot = False
# assorti = True # Bularning o'rniga 1 or 0 qo'ysak ham bo'ladi
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
 
# if choy: # agar choy olsa
#   print("Mijoz choy oldi.")
#   narx = narx + 3000
  
# if salat: # agar salat olsa
#  print("Mijoz salat oldi.")
#  narx = narx + 5000
   
# if non: # agar non olsa
#  print("Mijoz non oldi.")
#  narx = narx + 2000
    
# if kompot: # agar kompot olsa
#  print("Mijoz kompot oldi.")
#  narx = narx + 5000
     
# if assorti: # agar assorti olsa
#  print("Mijoz assorti oldi.")
#  narx = narx + 15000
#  print(f"Umumiy xarajatlar: {narx} so'm")

#  menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")

#     son = float(input("Istalgan son kiriting uning ildizini aniqlayman:"))
# ildiz = son**(1/2) #Bu orqali sonning ildizini aniqlaymiz
# print(f"{son} ning ildizi {ildiz} ga teng")

# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# print("\n")

# en_uz = {'apple':'olma', 'apricote':"o'rik", 'banana':"banan"}
# print(en_uz['apricote'])


# talaba_0 = {
#     'ism':'alijon',
#     'familya':'valijonov',
#     'yosh':22,
#     'fakultet':'geografiya',
#     'kurs':4
#     }

# #print(talaba_0.items())

# for key, value in talaba_0.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value} \n")

#     print("Yaqin do'slaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != 'ha':
#         break
    
# print("Do'slaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# print("\n")

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop() # pop bilan oxiridan boshlab ismlarni oladi.
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)


#     def toliq_ism_yasa(ism, familiya, otasining_ismi=''): # Bu yerda 
# # otasining_ismi ga bo'sh joy ochilgani yozsa ham yozmasa ham bo'ladi
#      """Toliq ism qaytaruvchi funksiya"""
#      if otasining_ismi:
#          toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#      else:
#          toliq_ism = f"{ism} {familiya}"
#      return toliq_ism.title()
# talaba1 = toliq_ism_yasa('olim','hakimov') 
# talaba2 = toliq_ism_yasa('hakim', 'olimov','abrorivich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# print("\n")





# # Yangi loyiha buni yana ham boyitsa bo'ladi

# def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narx':narxi}
#     return avto
# print("Saytimizda avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # Salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ",end=' ')
#     kompaniya=input("\nIshlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narxi=input("Narxi: ")
#     # Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
#     # Lug'at shakillantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
#     # Yana avto qo'shish-qo'shmasligini so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()} Yili:"
#           f"{avto['yil']}. {korobka} korobka. Narxi: {narx}")
    
    
    
    # print("New Project math moduli\n")

    # import math # Biz buni docs.python.org dan import qilib olib keldik
    # # matematik amallarni bajaradigan funksiya.
    # x=400
    # print(math.sqrt(x)) # sqrt - bu ildizini chiqaradi 400 ni.
    # print(math.pow(5,3)) # pow - bu darajasi degani bu yerda 5 ning 3 darajasi(kubi)
    # print(math.pi) # Bu pi ning qiymatini aniq ko'rsatib beradi 3.14 
    # print(math.log2(8)) # bu logorifmni hisoblaydi bunda 2 asosli log hisoblandi
    # print(math.log10(100)) # 10 asosli log hisoblandi

    # print("\n")

    # print("random moduli\n")

    # import random as r  # Bu yerda randomni qayta r deb nomlab olayabmiz va buning
    # # vazifasi tasodifiy raqam yoki ismlarni tanlaydi.
    # son = r.randint(0,100) # bu yerda 0 dan 100 gacha tasodifiy raqam tanlaydi.
    # print(son)

    # print("\n")

    # ismlar = ['olim', 'anvar', 'hasan', 'husan', 'ali', 'vali', 'salim', 'bakir']
    # ism = r.choice(ismlar) # choice ismlarni tasodifiy tanlaydi.
    # print(ism)
    # print(r.choice(ism)) # Bu tasodifiy tanlangan ism ichidagi harflarni yana 
    # # qaytadan tasodifiy tanlaydi

    # print("\n")

    # x = list(range(0,101,5)) # 0 dan 101 gacha raqamlar 5 qadam tashlab yozilgan jadval
    # print(x)
    # print(r.choice(x))

    # print("\n")

    # # shuffle() bu jadvalni aralashtirib tashlaydigan buyruq.
    # x = list(range(11)) # 11 gacha sonlar ro'yxati
    # print(x)
    # r.shuffle(x)
    # print(x)



# import random as r

# sonlar = r.sample(range(100),10) # 100 gacha sonlardan tasodifiy 10 ta tanlaydi.
# print(sonlar)
# # 1-usul
# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaradi"""
#     return x%2==0 # (%) bu amal bilan juft yoki toq sonligi tekshiriladi.
# # ikkiga bo'linadi qoldiq 0 bo'lsa juft aks holda toq son bo'ladi.
# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)
# # hamda bu yuqoridagi amallar bilan tanlangan 10 ta raqam ichidan juftlari  
# # tanlab olinadi.

# print("\n")
# # Yoki buning lambda bilan qisqaroq usuli.
# # 2-usul
# juft_sonlar = list(filter(lambda x: x%2==0,sonlar))
# print(juft_sonlar)

# print("\n")


# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", 'ari', "banan"]
# harf='a' # Istalgan boshqa harf ham qo'yishimiz mumkin
# mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
# print(mevalar_b) # Bunda a dan boshlanadigan mevalarni chiqaradi.

# print("\n")

# mevalar2 = list(filter(lambda meva:len(meva)<=4, mevalar))
# print(mevalar2) # Bu uzunligi 4 harfdan oshmagan mevalarni chiqaradi.




# # try va except dan ko'ra yana maqulroq variant yuqoridagi amal uchun.

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():  # Bu faqat butun son qabul qiladi
#         yosh = int(yosh)
#         break 
# print(f"Siz {2025-yosh} yilda tug'ilgansiz")

# # Butun son kiritilmaguncha dastur to'xtamaydi.

# # '20'.isdigit()  # butun son bo'lsa true 
# # Out[21]: True
# # '20,5'.isdigit()
# # Out[22]: False  # aks holda false deb chiqaradi consoleda tekshirganimizda.
# # 'besh'.isdigit()
# # Out[23]: False





















































