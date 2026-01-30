def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False
    
a = [1, 3, 5, 6, 45, 4 ,545,545 , 54]

new = list(filter(is_greater_than_9, a))
print(new)