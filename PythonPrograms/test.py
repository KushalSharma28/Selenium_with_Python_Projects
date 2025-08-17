# Palindrome check in Python

def is_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
word = input("Enter a word or phrase: ")

if is_palindrome(word):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
