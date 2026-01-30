numbers = [1, 2, 3, 25, 9, 21]

def square(x):
    return x * x

new = list(map(square, numbers))
print(new)