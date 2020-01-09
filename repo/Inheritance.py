class Employee():
    def __init__(self,firstName,salary,dept):
        print("init of Emp")
        self.firstName = firstName
        self.salary = salary
        self.dept = dept

    def showInfo(self):
        print("Emp Info")
        print("First name: {}\nSalary: {}\nDepartment: {}\n".format(self.firstName,self.salary,self.dept))

    def changeDept(self,deptName):
        self.dept = deptName


class Manager(Employee):
    def increaseSal(self,saltoAdd):
        self.salary += saltoAdd

manager = Manager("Cem",9000,"C# .NET")
manager.showInfo()
manager.changeDept("JavaScript")
manager.showInfo()

print(dir(manager))

manager2 = Manager("Serhat",3500,"Java")
manager2.increaseSal(500)
manager2.showInfo()

class Director(Employee):
    def __init__(self,firstName,salary,dept,supervises): #Overrided
        super().__init__(firstName,salary,dept)
        print("Inıt of Director")
        self.supervises = supervises
    def showInfo(self):
        print("Emp Info")
        print("First name: {}\nSalary: {}\nDepartment: {}\nNumber of supervises: {}\n".format(self.firstName,self.salary,self.dept,self.supervises)) #Overrided

    def increaseSal(self, saltoAdd):
        self.salary += saltoAdd

director = Director("Oguz",4000,"Node",10)
director.showInfo()

