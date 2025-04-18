# Problem-3.py

def generate_series(a):
    # If the input is even, reduce it by 1
    if a % 2 == 0:
        a -= 1

    # Generate 'a' odd numbers starting from 1
    count = 0
    num = 1
    while count < a:
        print(num, end=", " if count < a - 1 else "")
        num += 2
        count += 1

# Example usage
x = int(input("Enter a number: "))
generate_series(x)
