
def Modn(x,n): # x mod n
    store=[n] # contains 2^i*n
    while(True):
        n=n+n
        if(n<=x):
            store.append(n)
        else:
            break
    i=len(store)-1
    while(i!=-1):
        if(x>=store[i]):
            x=x-store[i]
        i=i-1
    return x
    
def removeFactorOf2(n): # n=2^h.t
    h=0
    while(Modn(n,2)==0):
        h=h+1
        n=n>>1
    return (h,n)

def power(x,n): # x^n
    a=x
    bin_string=[]
    while(n!=0):
        bin_string.append(Modn(n,2))
        n=n>>1
    c=1
    for i in range(0,len(bin_string)):
        if(bin_string[i]):
            c*=a
        a=a*a
    return c
def powerModN(x,n,m): # x^n mod m
    a=x
    bin_string=[]
    while(n!=0):
        bin_string.append(Modn(n,2))
        n=n>>1
    c=1
    for i in range(len(bin_string)):
        if(bin_string[i]):
            c=Modn(c*a,m)
        a=Modn(a*a,m)
    return c
# print(powerModN(91113,286540,286541))