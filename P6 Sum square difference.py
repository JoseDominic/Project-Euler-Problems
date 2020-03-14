#Project 6 Sum Square Square sum difference of integers upto n
def sumofsquares(n):
   sum1=0
   for i in range(1,n+1):
       sum1+=i**2
   return sum1
def squareofsum(n):    
    sum1=0
    for i in range(1,n+1):
        sum1+=i
    return sum1**2
n=int(input("Enter n:"))
D=abs(sumofsquares(n)-squareofsum(n))
print ("Answer:",D)
x=input("Press enter to continue:")
    
  
