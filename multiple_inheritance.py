class class1(object):
    def m(self):
        print("In class1")
    
class class2(class1):
    def m(self):
        print("In class2")

class class3(class1):
    def m(self):
        print("In class3")

class class4(class2,class3):
   pass
obj = class4()
obj.m()