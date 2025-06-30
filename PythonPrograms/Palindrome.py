def check_palindrome():
    """
    Checks if a user-entered string is a palindrome.
    A palindrome is a word, phrase, number, or other sequence of characters
    which reads the same backward as forward, e.g., "madam" or "racecar".
    The check is case-insensitive.
    """
    # Prompt the user to enter a string
    original = input("Enter a string to check if it is a palindrome: ")

    # Convert the string to lowercase to make the check case-insensitive
    # This ensures that "Madam" is treated the same as "madam".
    processed_string = original.lower()

    # Assume the string is a palindrome until proven otherwise
    is_palindrome = True

    # Initialize two pointers, one at the start and one at the end of the string
    start = 0
    end = len(processed_string) - 1

    # Loop to compare characters from both ends
    # The loop continues as long as the start pointer is less than the end pointer.
    while start < end:
        # Check if characters at start and end are different
        if processed_string[start] != processed_string[end]:
            is_palindrome = False  # Mark as not a palindrome
            break  # Exit the loop immediately if a mismatch is found

        # Move pointers towards the center
        start += 1  # Increment the start pointer
        end -= 1    # Decrement the end pointer

    # Output the result based on the is_palindrome flag
    if is_palindrome:
        print(f'The string "{original}" is a palindrome.')
    else:
        print(f'The string "{original}" is not a palindrome.')

# This block ensures that check_palindrome() is called only when the script is executed directly.
if __name__ == "__main__":
    check_palindrome()