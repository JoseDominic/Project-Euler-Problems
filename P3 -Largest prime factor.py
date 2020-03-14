#PEuler 3 Largest Prime Factor
import math
def checkprime(x):#function to check prime
    flag=-1
    i=int(math.sqrt(x))
    while(i>=2):
        if(x%i==0):
            flag=1
        i-=1
    if flag==-1:
        return 1
    else:
        return 0
assert checkprime(109)==1          
        
n=int(input("Enter the number:"))
if checkprime(n)==1:
    ans=n
else:
    i=int(math.sqrt(n))
    while i>0:
        if n%i==0:
            if checkprime(i)==1:
                ans=i
                break
        i-=1
print ("Largest prime factor is",ans)
y=input("Press any key to continue")
            
