from json import dumps
import pickle
class Animal(object):
    def __init__(self,no_of_legs,color):
        self.no_of_legs = no_of_legs
        self.color = color

class cat(Animal):
    def __init__(self, color):
        Animal.__init__(self,4,color)

C_p = cat("White")
My_pickled_C = pickle.dumps(C_p)
Meow = pickle.loads(My_pickled_C)
Meow.color = "Black"
print(str.format("Meow is {0}",Meow.color))
print(str.format("Cat is {0}",C_p.color))