#largest palindrome product of 2 n digit numbers
def palindrome(x):
    t=str(x)
    if (t[::1]==t[::-1]):
        return 1
    else:
        return -1
def div_by_ndigit(x,n):
    l=10**(n-1)
    u=int(n*"9")
    for i in range(u+1,l,-1):
        if x%i==0:
            return i
    return -1    
assert palindrome(9009)==1
assert div_by_ndigit(9009,2)==99
n=int(input("Enter no of digits:"))
u=(int(n*"9")* int(n*"9")) #finding greatest product of two n digit numbers
for i in range(u,(10**(n-1))**2,-1):
    if palindrome(i)==1:
        z=div_by_ndigit(i,n)   
        if (i/z)>10**(n-1) and (i/z)<int(n*"9"):  ##BUG to fix:Does not work when using if len(str(i/z))==n: instead   
                print ("Largest palindrome product of two",n,"digit numbers is",i)
                j=input("press enter to exit")
                exit()
    
    
        
    
