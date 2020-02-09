# In pyt, everything is object :)
#print(type([1,2,3]))

class Dog():
    #CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


mydog = Dog(breed="Lab",name = "Blackie")
ortherdog = Dog(breed="Huskie", name = "Gold")
print(type(mydog))
print(mydog.breed)
print(mydog.name)
print(mydog.species)


class Circle():
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
    
    def methodArea(self):
        return Circle.pi * self.radius * self.radius
    
    def set_radius(self,new_r):
        self.radius = new_r

myC = Circle(3)
print(myC.radius)
myC.radius = 100
print(myC.methodArea())

myC.set_radius(4)
print(myC.radius)