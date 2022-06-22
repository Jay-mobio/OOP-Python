from abc import ABC,abstractclassmethod
from collections import abc
class Polygon(ABC):
    @abstractclassmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("I have three sides")

class Pentagon(Polygon):
    def noofsides(self):
        print("I have five sides")

class Hexagon(Polygon):
    def noofsides(self):
        print("I have six sides")
    
class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have four sides")

R = Triangle()
R.noofsides()

P = Pentagon()
P.noofsides()

H = Hexagon()
H.noofsides()

Q = Quadrilateral()
Q.noofsides()