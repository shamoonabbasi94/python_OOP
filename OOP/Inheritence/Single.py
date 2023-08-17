class ParentClass:
    def method (self):
        print('this is from parent')
class ChildClass(ParentClass):
    pass

obj=ChildClass()
obj.method()
