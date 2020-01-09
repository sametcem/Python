
class Programmer():

    def __init__(self, firstName, lastName, phoneNo, salary, skills):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNo = phoneNo
        self.salary = salary
        self.skills = skills
    def showInfo(self):
        print("""
            Properties of Programmer
                
            First Name : {}
            Last Name : {}
            Phone Number: {}
            Salary: {}
            Technical Skills: {}
            
        """.format(self.firstName,self.lastName,self.phoneNo,self.salary,self.skills))
    def increaseSalary(self,amount):
        print("Salary is increasing")
        self.salary += amount
    def addSkill(self,newSkill):
        print("Technical Skill is adding")
        self.skills.append(newSkill)


prog1 = Programmer("Mustafa Murat", "Coşkun", 12345, 3000, ["Python", "C", "Java"])

prog2 = Programmer("Serhat", "Say", 23456, 3500, ["Matlab", "R", "SmallTalk"])

print(prog1.skills)
print(prog2.lastName)
prog1.showInfo()

prog3 = Programmer("Tommy", "Ford", 123321, 9000, ["Python", "Java", "JavaScript"])
prog3.addSkill("C#")
prog3.showInfo()
prog3.increaseSalary(999)
prog3.showInfo()