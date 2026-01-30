text ="Python"
print(f"{text:>10}") # Right align
print(f"{text:<10}") # Left align
print(f"{text:^10}")


pi =3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")


light = input("light : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("get ready")
elif(light == "green"):
    print("go")
else:
    print("light is broken")



class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.14 * self.radius * self.radius
        
    def parameter(self):
        return 2*3.14*self.radius
        
c1 = Circle(21)
print(c1.area())
print(c1.parameter())


class Employee: 
    def __init__(self, role, salary, account):
        self.role = role 
        self.salary = salary 
        self.account = account
    
    def show_details(self):
          print("role = ",self.role)
          print("salary = " ,self.salary)
          print("account = " ,self.account)

class Engineer(Employee):
     def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", 70000, "IT")

engg1 = Engineer("Elon Musk", 52)

engg1.show_details()

# e1 = Employee("developer", 50000, "123-456")
# e1.show_details()

