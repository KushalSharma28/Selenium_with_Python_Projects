def main():
    input_string = "good morning"
    vowel_count = 0
    temp = ""
    # Convert the string to lowercase to handle both uppercase and lowercase vowels
    input_string = input_string.lower()
    # Iterate through each character in the string
    for ch in input_string:
        # Check if the character is a vowel
        if ch in 'aeiou':
            temp += ch  # Store the vowel in temp variable
            vowel_count += 1  # Increase the counter
    # Print the results
    print("Vowels found:", temp)
    print("Total number of vowels:", vowel_count)
if __name__ == "__main__":
    main()