class person(object):
    def __init__(self,name):
        self.name = name
    
    def getname(self):
        return self.name
    
    def isEmployee(self):
        return False
    
class Employee(person):
    def isEmployee(self):
        return True

emp = person('Geek1')
print(emp.getname(),emp.isEmployee())

emp = Employee('Geek2')
print(emp.getname(),emp.isEmployee())