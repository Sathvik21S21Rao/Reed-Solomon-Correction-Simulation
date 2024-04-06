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
    
    
def power(x,n): # x^n
    a=sympy.Integer(x)
    bin_string=[]
    while(n!=0):
        bin_string.append(Modn(x,2))
        n=n>>1
    c=1
    for i in range(len(bin_string)-1,-1,-1):
        if(bin_string[i]):
            c*=a
        a=a*a
    return c