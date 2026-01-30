s = {34,33,5,7,4,37}

print(s)

s.add(45)
s.remove(5)
# s.remove(444) # this will throw an error
s.discard(4444) # but this will not throw the error
print(s)