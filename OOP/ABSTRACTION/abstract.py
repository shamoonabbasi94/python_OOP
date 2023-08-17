# Reporting parent class is developed by Shamoon
# class Vehicle:
#     def specification(self):
#         print('This is vehicle class specification')

# # Timmy is working on this
# class bike(Vehicle):
#     def specification(self):
#         print('This is bike class specification')

# # Nasson is working on this
# class Car(Vehicle):
#     def specification(self):
#         print('This is Car class specification')

# # James is working on this
# class Ambulance(Vehicle):
#     def Specification(self):
#         print('This is Ambulance class specification')

# obj_Ambulance=Ambulance()

# obj_Ambulance.specification()


from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def specification():
        pass
class Bike(Vehicle):
    def Price(self):
        return 1200
    def specification():
        return 'This is Bike class specification'
class Car(Vehicle):
    def Model(self):
        return '2018'
    @staticmethod
    def Price():
        return 2000
    def discount(self):
        return self.Price()*0.8
        
    def specification():
        return 'This is Car class specification'    


# obj_vehicle=Vehicle()
obj_bike=Bike()
print(obj_bike.Price())

obj_car=Car()
print(obj_car.Price())
print(obj_car.discount())