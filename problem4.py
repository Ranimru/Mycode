
def pal(x):
  l=str(x)
  for i in range(0,len(l)//2):
   if l[i]!=l[(len (l)-1)-i]:
      return False
  return True

D=[]
for z in range(500,1000):
     for y in range(500,1000):
       m=z*y
       if pal(m)==True:
        D.append(m)
print max(D)
         



 


 

