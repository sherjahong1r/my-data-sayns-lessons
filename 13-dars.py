"""
#13-dars: GitHub bilan ishlash
#Created on Sun Sep 21 21:53:08 2025
#author: Sherjahongir
"""


# GitHub ilovasini o'rnatish va u bilan tanishish.

# please hello world funksionini yozing

def hello_world():

    print("hello World")


# aylana yuzini hisoblaydigan funksion yozing   
def aylana_yuzi(radius):

    pi = 3.14159

    yuz = pi * radius ** 2

    return yuz
# consolega qanday chiqarishni ko'rsatamiz
radius = 5          
print("Aylana yuzi:", aylana_yuzi(radius))



# menga kalkulator kodlarini yozing

def add(a, b):

    return a + b                    
def subtract(a, b):

    return a - b    
def multiply(a, b): 

    return a * b
def divide(a, b):

    if b != 0:

        return a / b

    else:

        return "Nolga bo'lish mumkin emas!"
# kalkulatorni ishlatish
num1 = 10
num2 = 5    
print("Qo'shish:", add(num1, num2))
print("Ayirish:", subtract(num1, num2))             
print("Ko'paytirish:", multiply(num1, num2))
print("Bo'lish:", divide(num1, num2))
print("Bo'lish (nolga):", divide(num1, 0))
# GitHub Copilot qisqacha qo‘llanma

                        






# ✅ 1. Copilot taklifini avtomatik yozmasdan ko‘rish (Preview Mode)

# Agar taklif chiqsin, lekin Enter bosmasdan / avtomatik qo‘shilmasdan turib ko‘rmoqchi bo‘lsangiz:

# Ctrl + → (o‘ng o‘q) — keyingi taklif

# Ctrl + ← (chap o‘q) — oldingi taklif

# Tab — qabul qilish

# Esc — rad etish