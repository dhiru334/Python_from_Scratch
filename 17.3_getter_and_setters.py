class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property
    def first_name(self):
        l = self.name.split(" ")
        print(l)
        return l[0]
    
    @first_name.setter
    def set_first_name(self, first):
        l = self.name.split()
        new_name = f"{first} {l[1]}"
        self.name = new_name

e = Employee("Dheeraj Jadhav", 39999)

# print(e.first_name())
# e.set_first_name("Suraj")
# print(e.name)

print(e.first_name)
e.set_first_name = "Suraj"
print(e.name)

# e.project = 9
# print(e.project) 

