# Program to find fibonacci sequence for nth number using recursive approach.

def fibonacci_sequence(n):
    if (n < 0):
        print("Incorrect input")
    elif (n == 0):
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)


if __name__ == "__main__":
    n1 = int(input("Enter the required number:\n"))
    print(fibonacci_sequence(n1))
