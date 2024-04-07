# Description: This file contains the implementation of the Miller-Rabin primality test.
from sympy.stats import DiscreteUniform
from arithmeticOps import *
import time,random
def generateRandomPrime(x,T):
    while(True):
        n=random.randint(2,x)
        if(Primality(n,T).checkPrimality()):
            return n

class Primality:
    def __init__(self,x,T):
        self.x=x
        self.T=T
        self.h,self.t=removeFactorOf2(x-1)
       

    def _checkInWn(self,a): # Witness set test
        if(powerModN(a,self.x-1,self.x)==1):
            b=powerModN(a,self.t,self.x)
            if b==1:
                return True
            for i in range(0,self.h):
                if(b-self.x==-1):
                    return True
                if(b==1):
                    return False
                b=Modn(b*b,self.x)
            return False
        return False


    def checkPrimality(self):
        
        for i in range(0,self.T):
            random_int=random.randint(1,self.x-1)
            if not self._checkInWn(random_int):
                return False
        return True


# print(Primality(561,100).checkPrimality())

