
def check_prime():
    count=0
    if(num<2):
        print(f"{num} is not a prime number")
    else:
        for i in range(2, num):
            if(num%i==0):
                count+=1
                break

        if(count==0):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")
         


num=int(input("Enter a number : "))
check_prime()