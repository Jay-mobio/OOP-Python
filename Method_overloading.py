class first(object):
    def Hello(self, name = None):
        if name is not None:
            print('hello', name)
        else :
            print('Hello')
obj = first()
obj.Hello()
obj.Hello("Jay")
