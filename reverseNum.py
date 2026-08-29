def reverseNum(num):
    reverse=0
    for i in range(len(str(num))):
        lastDigit=num%10
        reverse=reverse*10+lastDigit
        num=num//10
    
    return reverse

num=int(input("Enter number : "))
print(f"the {num} in reverse order is : {reverseNum(num)}")

