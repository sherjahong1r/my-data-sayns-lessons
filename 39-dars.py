"""
39-dars: Python tashqi kutubxonasi (PyPi.org)
Created on Tue Oct 21 10:24:56 2025
@author: Sherjahongir
"""

# tashqi yoki ichi kutubxona degani boshqa bir dasturchilar tomonidan
# yozilgan turli xil tayyor funksiyalar, modullar va paketlarni yig'indisi.

# Tashqi kutubxonalarning asosiysi PyPi.org sahifasi hisoblandi


# pip install deep-translator
# Buni anakondaga o'rnatib olamiz
from deep_translator import GoogleTranslator

# pip install googletrans==3.1.0a0
#from googletrans import Translator
# Bu eski versiyasida qolgan va spyderning yangi versiyadan olib tashlangan 
# shuning uchun ishlamadi.

tarjimon = GoogleTranslator(source='auto', target='en')
# Translator bu maxsus klass (tarjimon esa obyekt)

matn_uz = 'Python - dunyodagi eng mashhur dasturlash tili'


# Istalgan matnni ingliz tiliga tarjima qilish uchun translate metodini chaqiramiz
tarjima = tarjimon.translate(matn_uz)
# Orginal matn
print("Original matn:", matn_uz)
# Tarjima
print("Tarjima:", tarjima)
# Orginal matn tili

#print(tarjima.src) # Bu src matining asl qaysi tilda ekanligini ko'rsatadi.



print("\n")


#  # # boshqa tilga tarjima qilish uchun dest parametridan foyadalanamiz
# tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
# print(tarjima_ru.text) # Bu 

# siz deep_translator kutubxonasini ishlatayapsiz, lekin googletrans
# kutubxonasining translate(..., dest='ru') va .text atributlarini 
# ishlatganingiz uchun xato chiqmoqda.
# deep_translator kutubxonasida:
# .translate() → to‘g‘ridan-to‘g‘ri string (matn) qaytaradi
# dest → yo‘q parametr (ya’ni dest='ru' ishlamaydi)
# .text → yo‘q atribut (shuning uchun AttributeError:
# 'str' object has no attribute 'text' chiqmoqda)


# Bu esa yangi from deep_translator import GoogleTranslatorda yozish yani
# to'g'ri varianti.
tarjimon_ru = GoogleTranslator(source='auto', target='ru')
tarjima_ru = tarjimon_ru.translate(matn_uz)
print("Tarjima (RU):", tarjima_ru)

print("\n")

# # Ingliztilidan tarjima 
matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = GoogleTranslator(source='uzbek', target='uz')
tarjima_uz = GoogleTranslator(source='auto', target='uz').translate(matn_en)
print("Ingliz tilidagi matn:", matn_en)
print("O'zbek tiliga tarjimasi:",tarjima_uz)

print("\n")

msg = "Tarjima uchun so'z kiriting (chiqib ketish uchun \"q\" deb yozing): "
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        # tarjima = tarjimon.translate(text, src='uz', dest='en')
        tarjima_uz = GoogleTranslator(source='auto', target='en').translate(text)
        print(tarjima_uz)
        
# NATIJASI       

# Tarjima uchun so'z kiriting (chiqib ketish uchun "q" deb yozing): men dasturlashni yaxshi ko'raman
# i love programming
# Tarjima uchun so'z kiriting (chiqib ketish uchun "q" deb yozing): 






print("\n")
# YANGI MODUL
# pip install requests  # Bu yordamida consolega o'rnatib olamiz

import requests
from pprint import pprint

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
pprint(r.text)

print("\n")

# restcountries API
country = "Uzbekistan"
#url = f"https://restcountries.eu/rest/v2/name/{country}"
url = f"https://restcountries.com/v3.1/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
# print(r_json.keys())
print(r_json['capital'])
# Hamda bundan so'ng consolega r_json deb yozsak uzbekistan haqida barcha 
# malumotlarni chiqarib beradi.



print("\n")

# import requests
# import googletrans

# url = "https://api.adviceslip.com/advice"
# r = requests.get(url)
# advice = r.json()['slip']['advise']
# print(advice)

# translator = googletrans.Translator()
# tarjima = translator.translate(advice, dest='uz')
# print(tarjima.text)
# Bu import googletrans yangi versiyada yo'q bo'lganligi sababli pastdagi
# yangi boshqa from deep_translator import GoogleTranslator dan foydalanayabman


from deep_translator import GoogleTranslator
import requests

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()['slip']['advice']
print("Inglizcha maslahat:", advice)

tarjima = GoogleTranslator(source='auto', target='uz').translate(advice)
print("O'zbekcha tarjimasi (uz):", tarjima)

# NATIJASI
# Inglizcha maslahat: To improve productivity, always have a shittier task to put off.
# O'zbekcha tarjimasi (uz): Hosildorlikni oshirish uchun har doim o'chirish uchun shitirer vazifasini bajaring.


print("\n")



# YANGI MODUL

# import requests
# from bs4 import BeautifulSoup

# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
# # pprint(r.text)

# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.prettify())
# news = soup.find_all(class_="news-title")
# #print(news[0].text)
# print(soup.prettify()[:1000])

# # Yuqoridagi kod toliq ishlamadi yangilanishlar qo'shilganligi sababli





print("\n")



# copyright Tim Ruscia aka techwithtim
# code from https://github.com/techwithtim/OpenCV-Tutorials

# import cv2

# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# while True:
#     ret, frame = cap.read()
    
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#         roi_gray = gray[y:y+w, x:x+w]
#         roi_color = frame[y:y+h, x:x+w] 
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
            
#     cv2.imshow('frame', frame)
    
#     if cv2.waitKey(1) == ord('q'):
#         break
#     cap.release()
#     cv2.destroyAllWindows()
# # Hullas bu ham camerani ochib insonning yuzini aniqlab beradigan cod 
# # Menda ishlamaganligining boisi camera ochmadi.



print("\n")



# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
# from uzwords import words

# # # Ikki so'z o'rtasida o'xshashlik foizini topish
# print(fuzz.ratio("salom","assalom"))
# print(fuzz.ratio("salom","salim"))

# Bu codlar ham ishlamadi

# Shuningdek pastda yana ikkita modul bor edi  bular ham hali ko'rganim yo'q
# Va qachondir bu darsni qaytadan oxirigacha ko'raman.



    
  

  

          


  


  
    
      
        
    


      
     