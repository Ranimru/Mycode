def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primearray=primes(6000) 

numbers=range(1,40)
squarenumbers=[]
for s in numbers:
  m=s*s
  squarenumbers.append(m)

Goldbach=[]
for i in primearray:
 for k in squarenumbers:
  c=i+2*k
  if c%2!=0:
   Goldbach.append(c)
   Goldbach.sort()

notGoldbach=[]
Numbers=range(0,6000)
for w in Numbers:
 if w%2!=0 and w not in Goldbach and w not in primearray:
  notGoldbach.append(w)
print notGoldbach




