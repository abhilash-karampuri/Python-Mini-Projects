#OTP creation
import random
n=int(input("enter the length of otp:"))
for x in range(0,n):
    ele=random.randint(0,9)
    print(ele,end="")  
