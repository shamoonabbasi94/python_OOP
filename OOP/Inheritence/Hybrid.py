class ParentClass:
    def method(self):
        print('This is from ParentClass')
class ParentClass2:
    def method2(self):
        print('This is from class ParentClass2')
class ChildClass(ParentClass,ParentClass2):
    pass
class GrandChildClass(ChildClass):
    pass

obj=GrandChildClass()
obj.method()  
obj.method2()  

