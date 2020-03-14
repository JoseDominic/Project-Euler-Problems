#Program to find the LCM of 1 to n
#BUG-Unefficient algorithm
def LCM(n):
    N=n
    while 1:
        i=2   
        while i<=n:
            if N%i==0:
                i+=1
            else: 
                break
        if i>n:
            return N
        N+=1    
        
n=int(input("Enter value of n:"))
t=LCM(n)
print ("LCM=",t)
x=input("Press enter to quit")
