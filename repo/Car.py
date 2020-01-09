class Car():
    model = "Ferrari Enzo"
    color = "Red"
    hP_power = 480
    cylinder = 9


car1 = Car()
print(car1.model)
print(Car.model) #default values

#print(dir(car1)) #auto_functions, init function will be generated as a default in fact.
print(car1.__class__)


#CONSTRUCTOR(__init__)

class Vehicle():
    model = "Ferrari Enzo"
    color = "Red"
    hP_power = 480
    cylinder = 9
    def __init__(self): #self is an reference which points the object
        print("Constructor __init__ called.")


vehicle1 = Vehicle()


class Auto():
    def __init__(self,model="Unknown",color="Unknown",hP_power=400,cylinder=4):
        print("Constructor __init__ called.")
        self.model = model
        self.color = color
        self.hP_power = hP_power
        self.cylinder = cylinder


auto1 = Auto("Porsche-992","grey",560,8)
auto2 = Auto("Audi A7","blue",645,10)
auto3 = Auto()

print(auto1.model)
print(auto2.model)
print(auto3.model)
print(auto3.hP_power)
