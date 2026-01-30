def remove_duplicates(number):
      return list(set(number))
nums = [1,2,2,3,4,5,1,2,3,4,3,5]
print("original list:", nums)
print("Without dupilcates:", remove_duplicates(nums))



# def remove_duplicates(numbers):
#     '''
#     Remove duplicates from a list using a set.

#     Parameters:
#         numbers (list): A list of integers or floats.

#     Returns:
#         list: A new list with duplicates removed.
#     '''
#     return list(set(numbers))

 
# nums = [1, 2, 3, 2, 4, 1, 5, 3]
# print("Original list:", nums)
# print("Without duplicates:", remove_duplicates(nums))
