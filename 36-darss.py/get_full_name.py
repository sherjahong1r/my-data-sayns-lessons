"""
36-dars: Funksiyalarni tekshirish. (unittest moduli)
Created on Thu Oct 16 23:11:14 2025
@author: Sherjahongir
"""


def get_full_name(ism, familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()

























