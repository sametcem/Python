# INHERITANCE

class Parent():
    def print_last_name(self):
        print("Roberts")


class Child(Parent):
    def print_firs_name(self):
        print("Bucky")

    def print_last_name(self): #OVERRIDING
        print("Tekin")



child = Child()
child.print_firs_name()
child.print_last_name()