
# Write a program to check if given character is digit or not.

def check_digit(num):
    if(num>='0' and num<='9'):
        print(f"{num} is a digit.")
    else:
        print(f"{num} is not a digit")

num=input("Enter a character : ")
check_digit(num)