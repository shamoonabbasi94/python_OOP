class ParentClass:
    def method (self):
        print('This is from class ParentClass')
class ParentClass2:
    def method2 (self):
        print('This is from class ParentClass2')
class ChildClass(ParentClass,ParentClass2):
    pass

obj=ChildClass()
obj.method()
obj.method2()
