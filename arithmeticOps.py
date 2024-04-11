
def Modn(x,n): # x mod n
    x1=x
    n1=n
    x=abs(x)

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
    if(x1<0):
        if(x!=0):
            return n1-x
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
def division(x,y):
    if(x<y):
        return 0
    x=x-Modn(x,y)
    q=1
    end=2
    while(y*end<x):
        temp=end+1
        end=end+(end-q+1)*2
        q=temp 

    while(q<=end):
        
        m=(q+end)>>1
        if(y*m>x):
            end=m-1
        elif(x>y*m):
            q=m+1
        else:
            return m
if __name__=="__main":
    print(division(100000,12312)==100000//12312)