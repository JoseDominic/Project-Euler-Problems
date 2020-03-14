#Project 7-nth prime no
import math
def isprime(n):
    if n==0 or n==1:
        raise (ValueError,"Neither prime nor composite")
    flag=1
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            flag=-1
            break
    if flag==1:
        return 1
    else:
        return -1
assert isprime(13)==1    
assert isprime(17)==1
def nthprime(n):
    count=0
    i=2
    while count!=n:
       if isprime(i)==1:
           count+=1
       i+=1
    return i-1
assert nthprime(5)==11
n=int(input("Enter n:"))
print (n,"th prime is ",nthprime(n))
x=input("Press enter to quit....")
    

    
