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
        
    

BaseClassObject = Employee("Base Class Name", 27)
print(BaseClassObject)
print(BaseClassObject.age)
print(BaseClassObject.name)
BaseClassObject.getEmployeeDetails()

FullTimeEmployeeObject = FullTimeEmployee("Full time Name", 27, "NCE")
FullTimeEmployeeObject.getEmployeeDetails()

ContractorObject = Contractor("Contractor Name", 27, "NCE")
ContractorObject.getEmployeeDetails()

InternObject = Intern("Intern Name", 27)
InternObject.getEmployeeDetails()