

import unittest
import math

round(math.pi, 3)

class Circle:
    def  __init__(self, raio:int):
        self.raio = raio

    @property
    def get_area(self) -> float:
        return (self.raio^2) * math.pi
    
    @property
    def get_perimeter(self) -> float:
        return 2*math.pi*self.raio


class CircleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.circle = Circle(raio = 5)

    def test_calculate_area(self):
       assert 78.54 == round(self.circle.get_area, 2)

    def test_calculate_perimeter(self):
        assert 31.416 == round(self.circle.get_perimeter, 3)

if __name__ == "__main__":
    unittest.main()