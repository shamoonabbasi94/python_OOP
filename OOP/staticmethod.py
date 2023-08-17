class parent:
    def method(self):
        return 2
    @staticmethod
    def method1():
        return 2
    def method2(self):
        return 5
    
class child(parent):
    def method3(self):
        return self.method1()+5
# obj=parent()
# print(parent.method2())
obj1=child()
print(obj1.method3())