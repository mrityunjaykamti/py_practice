def armstrongChk(num):
    original=num
    newNum=0
    for i in range(len(str(num))):
        lastdigit=num%10
        newNum=newNum+lastdigit**len(str(original))
        num=num//10

    if(newNum==original):
        print(f"{original} is an Armstrong number")
    else:
        print(f"{original} is not an Armstrong number")

num=int(input("Enter a number : "))
armstrongChk(num)