class a:
    def method (self):
        print('this is from class a')
class b(a):
    def method(self):
        print('this is from class b')
class c(a):
    def method(self):
        print('this is from class b')
class d(c,b):
    def dummy(self):
        print('This is from class d')

obj_b=d()
obj_b.method()  