
def checkprime(x):
   
    if x==0:
      return False
    if x==1:
      return False
    if x==2:
      return True
    for i in range(2,x):
      if x%i==0:
        return False
    return True



primearray=[]
L=[]
for s in range(2,10000000):

  if 600851475143%s==0:
  
    L.append(s)
    if checkprime(s)==True:
        primearray.append(s)

print L  
print primearray

