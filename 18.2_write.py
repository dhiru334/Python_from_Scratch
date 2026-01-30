# Write to a file called John.txt
# It should contain data about John

f = open("John.txt", "w")

string = '''
John is a nice guy. He lives in Nyc and works with Python
'''
f.write(string)

f.close()



