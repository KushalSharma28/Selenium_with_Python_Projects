# def fibonacci_series():
#     n = int(input("Enter value of n:"))
#
#     a, b, c = 0, 0, 1
#
#     print("Fibonacci Series:")
#
#     for _ in range(1, n + 1):
#         # In Python, simultaneous assignment makes swapping values concise
#         a, b, c = b, c, a + b
#         print(a, end=" ")
#
# if __name__ == "__main__":
#     fibonacci_series()

def fibonacci_series():
    """
    Generates and prints the Fibonacci series up to a given number n.
    """
    a, b = 0, 1  # Correct initialization of a and b

    try:
        n = int(input("Enter value of n: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if n < 0:
        print("Please enter a non-negative integer.")
        return

    print("Fibonacci Series: ", end="")

    for _ in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()  # Add a newline at the end for cleaner output


if __name__ == "__main__":
    fibonacci_series()

