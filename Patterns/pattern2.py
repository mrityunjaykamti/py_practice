# print this pattern (solid Rectangle)

# ********
# ********
# ********


row=int(input("Enter row : "))
col=int(input("Enter col : "))

for i in range(row):
    for j in range(col):
        print(" *",end="")
    print()