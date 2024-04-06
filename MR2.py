from sympy import Symbol
from sympy.stats import DiscreteUniform,sample
from arithmeticOps import *
class Primality:
    def __init__(self,x,T):
        self.x=x
        self.T=T
    def _checkInWn(self,a):
        if(Modn(power(a,self.x-1),self.x)==1):
            pass

    def checkPrimality(self):
        X=DiscreteUniform("X",range(1,self.x))
        random_int=X.pspace.sample()
        return random_int[X]




