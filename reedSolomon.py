from MR2 import *
from gmpy2 import mpz

def GlobalSetup(given_u,given_M):
    global k,primes,u,M
    u=mpz(given_u)
    M=mpz(given_M)
    k=100 # choice
    prime_upper_bound=1000000
    primes=[]
    while(len(primes)<k):
        rand=generateRandomPrime(prime_upper_bound,10)
        if rand not in primes:
            primes.append(rand)

def Transmit(items):
    l=random.randint(0,u*M)
    I=random.sample(items,l)
    b=[]
    for i in range(1,k+1):
        if i in I:
            b.append(random.randint(0,primes[i]-1))
        else:
            b.append(i)

    return b
# GlobalSetup(100,1000)
# print(primes)


        
       