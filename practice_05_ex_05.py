coordinates = (10, 20)

print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50 #tuple object does not support item assignment
corlist = list(coordinates)
corlist[0] = 50
print(corlist)

coordinates = tuple(corlist)
print(coordinates)


# coordinates = (10, 20)

# print(coordinates[0])
# print(coordinates[1])

# # coordinates[0] = 50
# corlist = list(coordinates)
# corlist[0] = 50
# coordinates = tuple(corlist)
# print(coordinates)



