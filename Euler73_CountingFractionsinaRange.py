"""
Euler73_CountingFractionsinaRange
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, 
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5,
 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions 
for d ≤ 12,000?:
"""
    
import math

def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

def list_primes(maxim):
    primes=[2,3,5,7]; 
    j=11
    while j<=maxim:
        if is_prime(j):
            primes.append(j)
        j+=1
    return primes;

primes=list_primes(6000);

def is_proper(num,denom):
    i=0
    while i<len(primes) and primes[i]<num and primes[i]<denom:
        if num%primes[i]==0 and denom%primes[i]==0:
            return False
        i+=1
    return True
    
def assemble_possibles():
    fracs=[]
    i=1
    while i<=12000:
        if i%500==0:
            print("passing through i being",i,"so there's another fifty thousand")
        j=2
        while j<=12000:
            fracs.append([i,j])
            j+=1
        i+=1
    print(len(fracs))
    return fracs
    
possibles=assemble_possibles()
    
def main():
    i=0
    count=0
    while i<len(possibles):
        if i%(10**6)==0:
            print("passing through",i,"so there's another million out of about 144 million")
        if is_proper(possibles[i][0],possibles[i][1]):
            if 1/3<possibles[i][0]/possibles[i][1]<1/2:
                count+=1
        i+=1
    print("the number of fractions between 1/2 and 1/3 is",count)
    return count
   
main()#--> the number of fractions between 1/2 and 1/3 is 7295372         
