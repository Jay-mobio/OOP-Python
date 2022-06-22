import pickle
class Animal(object):
    def __init__(self,no_of_legs,color):
        self.no_of_legs = no_of_legs
        self.color = color

class cat(Animal):
    def __init__(self, color):
        Animal.__init__(self,4,color)

C = cat("White")
print(str.format("my cat is {0} and has{1} legs", C.color, C.no_of_legs))
pickle_C = pickle.dumps(C)
print("Would you like to see her pickled? Here is she!")
print(pickle_C)