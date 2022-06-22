class parent(object):
    def __init__(self):
        self.value = 'Inside the parent'
    
    def show(self):
        print(self.value)

class child(parent):
    def __init__(self):
        self.value = 'Inside the child'

    def show(self):
        print(self.value)

obj1 = parent()
obj2 = child()

obj1.show()
obj2.show()