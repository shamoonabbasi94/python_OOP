from multipledispatch import dispatch

class parent():
    @dispatch(int,int)
    def method(self,x,y):
        return '2 arg response is {}'.format(x+y)
    @dispatch(int,int,int)
    def method(self,x,y,z):
        return '3 arg response is {}'.format(x+y+z)

obj=parent()
response2=obj.method(1,2)
response=obj.method(2,2,3)

print(response)
print(response2)

