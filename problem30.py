
X=[]
for x in range(2,2000000):
  l=str(x)
  M=[]
  
  for i in range(0,len(l)):
   
   c=int(l[i])**5
   M.append(c)
  #print M
  #print sum(M)
   
  if sum(M)==x:
     
     X.append(x)
print X
print sum(X)
