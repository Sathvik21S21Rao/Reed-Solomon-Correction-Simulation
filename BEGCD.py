from arithmeticOps import Modn , power
from gmpy2 import mpz

opt_r = []
opt_s = []
opt_t = []
 
def begcd(a,b):
    global opt_r,opt_s,opt_t
    opt_r.clear()
    opt_s.clear()
    opt_t.clear()
    e = 0
    r=0
    t=0
   
    while Modn(a,2)==0 and Modn(b,2)==0:
        e+=1
        a = a>>1
        b = b>>1
       
        
    
    a2 , b2 = a , b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    
    while b!=0:
        while Modn(a,2)==0:
            a=a>>1
            if(Modn(s1,2)==1 or Modn(t1,2)==1):
                s1 , t1= s1+b2 , t1-a2
            
            s1 >>=1
            t1 >>=1
            
            assert s1*a2+t1*b2==a
        
        while Modn(b,2)==0:
            b=b>>1
            if(Modn(s2,2)==1 or Modn(t2,2)==1):
                s2 , t2 = s2+b2 , t2-a2
            s2 >>=1
            t2 >>=1
            assert s2*a2+t2*b2==b
             
        if a > b:
            a, b = b, a
            s1 , s2 = s2 , s1
            t1 , t2 = t2 , t1
            
        b-=a
        s2-=s1
        t2-=t1
        
        
        opt_r.append(a*power(2,e))
        opt_s.append(s1)
        opt_t.append(t1)
    
        
    return [a * power(2,e),s1,t1]
        

        
if __name__=="__main__":
    print(begcd(47247096489788,22160927059))
