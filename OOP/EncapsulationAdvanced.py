class encap:
    __attr=10
    attribute=6
    def method(self):
        return self.__attr
class encapChild(encap):
    def method1(self):
        return self.method()

obj_encapchild=encapChild()
print(obj_encapchild.method1())

mydict={}
