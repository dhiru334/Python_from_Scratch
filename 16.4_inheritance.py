class Animal:   # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

# a = Animal("Dog")
# a.speak()

class Dog(Animal):  # This is how inheritance is done in Python
    def speak(self):
        print("Woof!")


d = Dog("Bruno")
d.speak()
print(d.location)
