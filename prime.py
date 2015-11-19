

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



Array=range(0,100)
primearray=[]
for x in Array:
    if checkprime(x)==True:
        primearray.append(x)

print primearray
