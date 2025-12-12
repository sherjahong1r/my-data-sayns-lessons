import unittest # Bu qism hech qachon o'zgarmaydi
from get_full_name import get_full_name # Bu qism faqat import qilmoqchi bo'lgan
 # fayl nomini o'zgartiramiz.
class NameTest(unittest.TestCase): # Bu ham o'zgarmaydi
    def test_toliq_ism(self): # Qolganlari nimani tekshirishga qarab o'zgaradi
        name = get_full_name('alijon','valiyev')
        self.assertEqual(name,'Alijon Valiyev')
        
    def test_otasining_ismi(self):
        name = get_full_name('alijon','valiyev','olimovich')
        self.assertEqual(name,'Alijon Olimovich Valiyev')
        
unittest.main() # bu ham o'zgarmaydi.

# NATIJASI
# Reloaded modules: get_full_name
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# OK



















