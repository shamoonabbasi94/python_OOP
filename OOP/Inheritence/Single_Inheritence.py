class ParentClass:
    def addition(self,x,y):
        return x+y


# obj=ParentClass()
# out=obj.addition(1,2)
# print(out)

class Child1(ParentClass):
    def multiply(self,x,y):
        out=self.addition(x,y)
        return out*3

obj=Child1()
out=obj.multiply(3,3)
print(out)