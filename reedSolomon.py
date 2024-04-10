from MR2 import *
from gmpy2 import mpz
from CRT import CRT
from BEGCD import *
from functools import reduce
from EGCD import *
from Thues import thue
class ReedSolomonSimulation:
    def GlobalSetup(self,given_u,given_M):
        
        self.u=given_u
        self.M=mpz(given_M)
        self.k=20 # choice
        prime_upper_bound=10000
        self.primes=[]
        while(len(self.primes)<self.k):
            rand=generateRandomPrime(prime_upper_bound,10)
            if rand not in self.primes:
                self.primes.append(rand)
        self.primes.sort()

    def ReedSolomonSend(self,a):
        try:
            self.u
            self.M
            self.k
            self.primes
        except NameError:
            raise Exception("GlobalSetup was not done")
        a_i=[]
        for i in range(self.k):
            a_i.append(Modn(a,self.primes[i]))
        
        self._Transmit(a_i)
        

    def _Transmit(self,items):
        
        l=random.randint(0,int(self.u*self.k))
        print("L:",l)
        self.P_upper_bound=1
        for i in range(l-1):
            self.P_upper_bound*=self.primes[-(1+i)]

        self.n=2*self.M*self.P_upper_bound*self.P_upper_bound+100 # n>2MP^2

        I=random.sample(range(0,self.k),l)
        self.b_i=[]
        for i in range(self.k):
            if i in I:
                self.b_i.append(random.randint(0,self.primes[i]-1))
            else:
                self.b_i.append(items[i])

        return self.b_i
    def ReedSolomonReceive(self):
        try:
            self.b_i 
        except NameError:
            raise Exception("No data was transmitted")
        
        self.recovered_message=CRT(self.primes,self.b_i)
        self.n=reduce(lambda x,y:x*y,self.primes)

        assert self.n>2*self.M*self.P_upper_bound*self.P_upper_bound
        
        result=thue(self.n,self.recovered_message,self.M*self.P_upper_bound,self.P_upper_bound)
        
        if(Modn(result[0],result[1])==0):
            return division(result[0],result[1])
        else:
            raise Exception("Cannot recover the message")
if __name__=="__main__":
    rs=ReedSolomonSimulation()
    rs.GlobalSetup(0.2,100000000000)
    rs.ReedSolomonSend(99999999)
    print(rs.ReedSolomonReceive())


        
       