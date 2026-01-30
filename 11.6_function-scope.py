def sum(a,b):
    # a and b are local variables
    c= a+b
    z = 1 
    # It creates a local variable called z which is destroyed after this function returns
    return c

def greet():
    z = 32
    #local variable
    print("Hello")


z = 8 
# z is a local variable
print(sum(4,5))

print(z)

