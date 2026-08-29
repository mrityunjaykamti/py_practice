# Write a program to print the smallest number of two.

def smallest(num1,num2):
    if(num1<num2):
        return num1
    else:
        return num2

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))

print(f"the smallest number between {num1} and {num2} is : {smallest(num1,num2)}")
