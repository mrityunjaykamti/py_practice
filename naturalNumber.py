
# Write a program to check if the given number is a natural number.

def check_natural_number(num):
    if(num>=1):
        print(f"{num} is a natural number.")
    else:
        print(f"{num} is not a natural number.")

num=int(input("Enter a number : "))
check_natural_number(num)