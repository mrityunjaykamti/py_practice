# print this pattern (increasing star triangle)

# *
# **
# ***
# ****
# *****


num=int(input("Enter number : "))

for i in range(1,num+1):
    for j in range(i):
        print(" *",end="")
    print()