# Problem-2.py

def print_odd_numbers(n):
    count = 0
    number = 1
    while count < n:
        print(number, end=", " if count < n - 1 else "")
        number += 2
        count += 1

# Enter the input
num = int(input("Enter how many odd numbers you want: "))
print_odd_numbers(num)
