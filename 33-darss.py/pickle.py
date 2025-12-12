"""
33-dars:  (Pickle)
Created on Tue Oct 14 00:20:41 2025
@author: Sherjahongir
"""



import pickle

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)
print(talaba2)


# (wb) - write binary = (ikkilik sanoq sistemasida yozish degani)
# (rb) - read binary = (ikkilik sanoq sistemasini o'qish degani)



# NATIJASI
# {'ism': 'hasan', 'familiya': 'husanov', 'tyil': 2003, 'kurs': 2}
# {'ism': 'alijon', 'familiya': 'valiyev', 'tyil': 2004, 'kurs': 1}


print('\n')


import pickle

# 1. Ma’lumot tayyorlaymiz
avtolar = [
    {"model": "Malibu", "yil": 2022, "narx": 33000},
    {"model": "Cobalt", "yil": 2020, "narx": 15000}
]

# 2. Faylga yozamiz
with open("avtolar.pkl", "wb") as f:
    pickle.dump(avtolar, f)

# 3. Fayldan qayta o‘qiymiz
with open("avtolar.pkl", "rb") as f:
    yangi_avtolar = pickle.load(f)

print(yangi_avtolar)














