from math import *
L=[]
for i in range(1,500):
  for j in range(1,500):
    for k in range(1,500):
       if k==sqrt(i**2+j**2):
          p=i+j+k
          L.append(p)

M=[] 
for x in L:
  c=L.count(x)
  M.append(c)
  b=max(M)
  d=M.index(b)   
  
print 'Perimeter=',L[d]
print 'Maximum no. of solutions is',(max(M)/2)
