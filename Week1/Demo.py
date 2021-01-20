import this

class Employee:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def getEmployeeDetails(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class FullTimeEmployee(Employee):
    def __init__(self,name,age,designation):
        super().__init__(name,age)
        self.designation = designation

    def getEmployeeDetails(self):
        print("___Full Time Employee Details__")
        super().getEmployeeDetails()
        print("Designation :", self.designation)

class Contractor(Employee):
    def __init__(self,name,age,designation):
        super().__init__(name,age)
        self.designation = designation

    def getEmployeeDetails(self):
        print("___Contract Employee Details__")
        super().getEmployeeDetails()
        print("Designation :", self.designation)

class Intern(Contractor):
    def __init__(self,name,age):
        super().__init__(name,age,"Intern")

    def getEmployeeDetails(self):
        print("___Intern Employee Details__")
        super().getEmployeeDetails()
        
    

a = Employee("Sucharitha", 27)
print(a)
print(a.age)
print(a.name)
a.getEmployeeDetails()

b = FullTimeEmployee("Sucharitha", 27, "NCE")
b.getEmployeeDetails()

c = Contractor("Sucharitha", 27, "NCE")
c.getEmployeeDetails()

d = Intern("Sucharitha", 27)
d.getEmployeeDetails()