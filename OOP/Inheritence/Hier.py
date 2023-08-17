class ParentClass:
    def method (self):
        print('this is from parent')
class ChildClass(ParentClass):
    pass
class ChildClass2(ParentClass):
    pass

obj=ChildClass()
obj2=ChildClass2()

obj.method()
obj2.method()
