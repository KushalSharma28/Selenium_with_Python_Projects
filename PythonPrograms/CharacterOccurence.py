# def calculate_concurrence(input_string):
#     char_counts = {}
#
#     for c in input_string:
#         char_counts[c] = char_counts.get(c, 0) + 1
#
#     return char_counts
#
# if __name__ == "__main__":
#     input_string = "This is a test string"
#     char_counts = calculate_concurrence(input_string)
#
#     print("Character Concurrence in the string:")
#     for char, count in char_counts.items():
#         print(f"Character '{char}': {count}")

def main():
    input_string = input("Enter a string: ")
    char_count_map = {}

    for c in input_string:
        char_count_map[c] = char_count_map.get(c, 0) + 1

    print("Character Concurrence:")
    for key in char_count_map:
        print(f"{key}: {char_count_map[key]}")

if __name__ == "__main__":
    main()
