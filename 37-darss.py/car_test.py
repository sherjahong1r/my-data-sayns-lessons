"""
37-dars: KLASSNI TEKSHIRISH
Created on Sun Oct 19 11:08:10 2025
@author: Sherjahongir
"""


from car import Car
import unittest

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    def setUp(self):
        make = "GM"
        self.model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make,self.model,year)
        self.avto2 = Car(make,self.model,year,price=self.price)
        
    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertEqual(self.model,self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEquals metodi bilan bilan tekshiramiz
        self.assertEqual(0,self.avto1.get_km())
        # avto2 narhini tekshiramiz
        self.assertEqual(self.price,self.avto2.price)
# yuqoridagi bitta test

    
        
    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price,self.avto2.price)
#  Bu ikkinchi test. 
        
        
        
    def test_add_km(self):
        # 1 Musbat qiymat berib ko'ramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        self.avto1.add_km(5000)
        self.assertEqual(15000,self.avto1.get_km())
        # 2 Manfiy qiymat berib ko'ramiz
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
# Bu uchinchi test
    
        
unittest.main()


#  NATIJASI

# %runfile C:/Users/Owner/Desktop/Python.py/37-darss.py/car_test.py --wdir
# Reloaded modules: car
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.002s

# OK



















