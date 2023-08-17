class any:
    __x=5
    def method1(self):
        print('bonus is {}'.format(self.__x*self.__addition()))
    def __addition(self):
        return 25

obj=any()
print(obj.__x)
# obj.__addition()
obj.method1()   
