class parent():
    def method(self,x,y):
        return '2 argument response is {}'.format(x+y)
        #Desired Result Is 10
    def method(self,x,y):
        return '3 argument response is {}'.format(x*y)
        #Desired Result Is 25

obj=parent()

response=obj.method(5,5)
print(response)
