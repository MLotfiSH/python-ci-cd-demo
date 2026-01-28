import sys

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add.py <number1> <number2>")
        sys.exit(1)
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Error: Both arguments must be numbers")
        sys.exit(1)
    
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")