class ParentClass:
    def addition(self,x,y):
        return x+y

class Child1(ParentClass):
    def multiply(self,x,y):
        out=self.addition(x,y)
        return out*3

class Child2(ParentClass):
    def square(self,x,y):
        out=self.addition(x,y)
        return out**2

obj=Child2()
output=obj.square(2,2)
print(output)
