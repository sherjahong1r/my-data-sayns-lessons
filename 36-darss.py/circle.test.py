import unittest
from circle import getArea, getPerimetr

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertEqual(getArea(5),78.53975)
        self.assertAlmostEqual(getArea(10),314.157,2) # bu bilan deyarli teng 
# bo'lsa ham Ok deb chiqar degani. Chunki har doim ham yuqori aniqlikda hisob-
# lay olmasligimiz mumkin. Shuningdek oxirida verguldan keyin nechi son qo'ysak
# shungacha aniq hisoblaydi.

    def test_perimetr(self):
        self.assertAlmostEqual(getPerimetr(10), 62.8318)
        self.assertAlmostEqual(getPerimetr(4), 25.13272)

unittest.main()


#  oxiridagining asl javobi 314.159 (314.157,2) bu edi lekin verguldan keyin
#  2 xonalini  aniq qolgani shunga yaqin bo'lsa Ok deb chiqaradi.

# NATIJASI

# Reloaded modules: circle
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.002s

# OK
