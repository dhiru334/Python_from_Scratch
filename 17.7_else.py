try:
    a = 365/0

except Exception as e:
    print(e)

#get executed when there is no error in the try block 
else:
    print("Hey I am good")