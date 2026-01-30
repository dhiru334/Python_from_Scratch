

# Class : Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives , father's name etc

# Object: Specific isinstance created from the template(class.). Eg. Form which contains the data DHeeraj

class Employee:
    company =  "HP"

    def get_salary(self): #self is important here because self is a way to reference the object of the class which is being created
        return 2005
    
e = Employee()  # An object of class Employee is create here 
print(e.get_salary())  # Employee e's get salary method is called 

e2 = Employee()
print(e2.get_salary())
print(e2.company)

