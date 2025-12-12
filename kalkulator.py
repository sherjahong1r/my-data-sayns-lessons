"""
Created on Sun Oct 26 10:00:36 2025
Kalkulator yasash
@author: Sherjahongir
"""
    
print('\n')
print('\n')
    
    
    
print("Matematik amallarni bajaramiz.")

while True:
    savol = input(
        "\nQo'shish uchun (+),\n Ayirish uchun (-),\n Ko'paytirish uchun (x),\n"
        "Bo'lish uchun (:),\n"
        "Tugatish uchun (end) deb yozing: namuna (+/-/x/:/end): >>>")
    
    
    if savol == "+":
        try:
           son1 = int(input("\nbirinchi sonni kiriting? >>>"))
           son2 = int(input("ikkinchi sonni kiriting? >>>"))
           javob = son1 + son2
           print(f"\nJavob: {son1} + {son2} = {javob} ✅")
        except ValueError:
           print("Siz faqat son kiritishingiz mumkin!❎"
                 "\nQaytadan urining? 🔁")
        else:
            print("Misolingiz bajarildi!⤴")
            
           
    elif savol == "-":
        try:
           son1 = int(input("\nbirinchi sonni kiriting? >>>"))
           son2 = int(input("ikkinchi sonni kiriting? >>>"))
           javob = son1 - son2
           print(f"\nJavob: {son1} - {son2} = {javob} ✅")
        except ValueError:
           print("Siz faqat son kiritishingiz mumkin!❎"
                 "\nQaytadan urining? 🔁")
        else:
            print("Misolingiz bajarildi!⤴")
            
           
    elif savol == "x":
        try:
           son1 = int(input("\nbirinchi sonni kiriting? >>>"))
           son2 = int(input("ikkinchi sonni kiriting? >>>"))
           javob = son1 * son2
           print(f"\nJavob: {son1} * {son2} = {javob} ✅")
        except ValueError:
           print("Siz faqat son kiritishingiz mumkin!❎"
                 "\nQaytadan urining? 🔁")
        else:
            print("Misolingiz bajarildi!⤴")
           
            
    elif savol == ":":
        try:
           son1 = int(input("\nbirinchi sonni kiriting? >>>"))
           son2 = int(input("ikkinchi sonni kiriting? >>>"))
           javob = son1 / son2
           print(f"\nJavob: {son1} : {son2} = {javob} ✅")
        except ValueError:
           print("Siz faqat son kiritishingiz mumkin!❎"
                 "\nQaytadan urining? 🔁")        
        except ZeroDivisionError:
           print("\nNolga bo'lib bo'lmaydi!❎"
                 "\nQaytadan urining? 🔁")
        else:
            print("Misolingiz bajarildi!⤴")
            
            
    elif savol == "end":
        print("\n\nThank you for your atention!🙂")
        break    
    else:
        False
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    