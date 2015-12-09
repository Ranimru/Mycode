def prod(L):
   r=1
   for i in L:
    r*=i
   return r

def fac(S):
   if S==0:
    return 1
   M=[]
   for j in range(1,(S+1)): 
    M.append(j)
    B=prod(M)
   return B 

X=[]
for x in range(3,50000):
  
  l=str(x)
  M=[]
  for i in range(0,len(l)):
   c=int(l[i])
   b=fac(c)
   M.append(b)
  #print M
  #print l
  #print sum(M)
    
  if sum(M)==x:
     X.append(x)
print X
print sum(X)


