class Parent:
    def method(self):
        return 5
class Child1(Parent):
    def calculation(self,x,y):
        return self.method() +x+y
    def method(self):
        return 100
obj=Child1()
print(obj.calculation(10,20))

