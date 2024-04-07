from MR2 import *

def GlobalSetup(given_u,given_M):
    global k,primes,u,M
    u=given_u
    M=given_M
    k=5 # choice
    primes=[]
    while(len(primes)<k):
        rand=generateRandomPrime(len(M)*len(M),1000)
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


        
       