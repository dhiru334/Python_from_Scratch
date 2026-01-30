class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)
    
    @staticmethod   # Static Method
    def sum(a, b):
        return a+b
    
    # Class Method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Jack", 45000)
e2 = Employee("Lily", 46000)

# print(Employee.company)
# print(Employee.name)  #this will throw an error

# # e1.print_info()
# e2.print_info()

# print(e1.sum(5,7))

print(Employee.company)
e1.change_company("Acer")
print(Employee.company)