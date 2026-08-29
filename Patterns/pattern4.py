# Print this pattern ... Decreasing star triangle

# *****
# ****
# ***
# **
# *

num=int(input("Enter number : "))

for i in range(num):
    for j in range(num-i):
        print(" *",end="")
    print()