def prod(L):
   r=1
   for i in L:
    r*=i
   return r

n=100
M=[]
for i in range(1,(n+1)):
  
  l=1
  l*=i
  M.append(l)
   
print prod(M)

x=prod(M)
l=str(x)
S=[]
for i in range(0,len(l)):
  S.append(int(l[i]))

print sum(S)


 
