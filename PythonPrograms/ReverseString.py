# Reverse String

# text="hello world"
# reversed_text=text[::-1]
#
# print("original= ", text)
# print("Reversed= ", reversed_text)

# Reverse string without slicing, indexing, or inbuilt functions

text = "Hello World"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text  # prepend each character

print("Original:", text)
print("Reversed:", reversed_text)
