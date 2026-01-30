text = "coding in python is fun"
sum = 0
vowels = ['a','e','i','o','u']
for char in text.lower():
    if(char in vowels ):
        sum +=1

print(f"There r {sum} vowels in this text")




# sentence = "Coding in Python is fun"
# sum = 0
# vowels = ['a', 'e', 'i', 'o', 'u']

# for char in sentence.lower(): 
#     if(char in vowels):
#         sum += 1

# print(f"There are {sum} vowels in this sentence")