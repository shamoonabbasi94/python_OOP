class ParentClass:
    def method (self):
        print('this is from parent')
class ChildClass(ParentClass):
    pass
class GrandChildClass(ChildClass):
    pass

obj=GrandChildClass()
obj.method()

