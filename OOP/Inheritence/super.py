class parent:
    def show(self):
        print('this is parent 1 class')

class child1(parent):
    def show(self):
        print('This is child class')
    def display(self):
        super().show()


        # print('this is child class')

obj=child1()
obj.display()

