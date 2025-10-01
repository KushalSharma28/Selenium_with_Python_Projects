# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separate lists for even and odd numbers
# even_numbers = []
# odd_numbers = []
#
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
#
# print("Original list:", numbers)
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)

# Original list
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Odd numbers using list comprehension
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Original list:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
