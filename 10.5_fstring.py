# string formatting 

template = "Dear {}, You r awesome. Take this {}$ bag"
a = "Dheeraj"
a1 = 10000
b = "Suraj"
b1 = 1000
c = "Jadhav"
c1 = 1999

s1 = template.format(a, a1)
print(s1)

print(f"{a} you r awesome and take this {a1}$ bag")