from arithmeticOps import division
def thue(n,b,rmax,tmax):
    if(n<b):
        n,b=b,n
    s0=1
    s1=0
    t0=0
    t1=1
    r0=n
    r1=b
    if(r0<rmax):
        return [r0,abs(t0)]
    if(r1<rmax):
        return [r1,abs(t1)]
    while(r1!=0):
        q=division(r0,r1)
        r=r0-q*r1
        s=s0-q*s1
        t=t0-q*t1
        if(r<rmax):
            return [r,abs(t)]
        r0=r1
        r1=r
        s0=s1
        s1=s
        t0=t1
        t1=t
if __name__=="__main__":
    print(thue(1888865960406168288505398222400818257775292507541277707906346865361,304298599341330493492722680341658913089787238649135255897983876019,6201315100000000000,62013151))