"""
33-dars: Fayllar bilan ishlash (Pickle)
Created on Tue Oct 14 00:20:41 2025
@author: Sherjahongir
"""


# Nima uchun biz with dan foydalanayabmiz chunki biz with open() qilmasak
# faylni oxiriga 
# fayl = open('test.txt', 'w')
# fayl.write('Salom!')
# fayl.close()   
# qilishimiz kerak agar fayl.close() qilmasak boshida yozgan kodlar saqlanmay
# qolishi mumkin 
# Shuning uchun with open() ning vazifasi bir yo'li yopib ketadi va 
# tavsiya qilinadi.


import pi_file

with open('pi.txt') as file:
    pi = file.read()
    
    
#print(pi_file.pi)
print(pi)

pi = pi.rstrip()
pi = pi.replace('\n','')
pi = float(pi)  # stringdan float ko'rinishiga o'tkazdik
print(pi)

# NATIJASI 
# 3.141590987654
# 098765433333
# 098765456789
# 3.141590987654099
print('\n')



# YANGI BOSQICH YANI IMPORT QILISH




filename = '../33data/talabalar.txt' # import qilish usuli.
# Buni 33data folder ichidagi talabalar degan fayl import qilingan

# with open(filename) as file:
#     for line in file:
#         print(line) # Bu usul print bilan qatorma qator chiqaradi.


with open(filename) as file:
    talabalar = file.readlines()
print(talabalar) # Bu usul bilan ro'yxatga joylanadi

# ['\n', 'Alijon Valiyev\n', 'Hasan Olimov \n', 'Hasan Furqatov\n',
#  "G'ani Salimov\n", "Yo'lchi Sobirov"]

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar) # bu metod oxiridagi \n ni olish uchun

# NATIJASI
# ['', 'Alijon Valiyev', 'Hasan Olimov', 'Hasan Furqatov', "G'ani Salimov", 
#  "Yo'lchi Sobirov"]
print('\n')



# YANGI BOSQICH  yani matnga o'zgartirish kiritsak bo'ladi





faylnomi = 'new_file.txt' # Bunda yangi fayl yaratilgan.
ism = 'Olimjon Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl: # 'w' bilan write yani yangi faylga yozish mumkin
    fayl.write(ism+ '\n')        # yuqoridagilarda w bo'lmagani uchun faqat 
    fayl.write(str(tyil)+'\n')   # read yani o'qiladi
print(fayl)

# Agar bunda w bo'lsa va yangi o'zgartirish kiritmoqchi bo'lsak eskisi o'chib
# ketadi


with open(faylnomi,'a') as fayl: # a - append (qo'shish degani)
    fayl.write('Alijon Shamshiyev\n')
    fayl.write('2000')
print()
# Bunda esa a metodi bilan yangi o'zgartirish kiritsak ham eskisi o'chmaydi
# va davom etib ketaveradi


with open(faylnomi, 'r') as fayl: # r - read (o'qish)
    mazmun = fayl.read()
    print("📄 Fayl tarkibi:\n")
    print(mazmun)
# Bu yerda r bilan mavjud bo'lgan barcha matnlarni chiqarishimiz mumkin
print('\n')



# PICKLE BILAN ISHLASH ingliz tilida tarjimasi (TUZLANGAN BODRING) degani



import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('talaba1','wb') as file:
    pickle.dump(talaba1,file)
#    pickle.dump(talaba2,file)

# Buning davomi va natijasi pickle.py degan oxiridagi faylda chiqadi.


# (wb) - write binary = (ikkilik sanoq sistemasida yozish degani)
# (rb) - read binary = (ikkilik sanoq sistemasini o'qish degani)



















