L=[]
for i in range(0,190000):
    x=str(i)
    if x==0:
     L.append(x)
    if i<10:
     L.append(x)
    if i>=10 and i<100:
     d=list(x)
     for j in range(0,2):
      L.append(d[j])
    if i>=100 and i<1000:
      d=list(x)
      for j in range(0,3):
       L.append(d[j])
    if i>=1000 and i<10000:
      d=list(x)
      for j in range(0,4):
       L.append(d[j])
    if i>=10000 and i<100000:
      d=list(x)
      for j in range(0,5):
       L.append(d[j])
    if i>=100000 and i<1000000:
      d=list(x)
      for j in range(0,6):
       L.append(d[j])

print L
print int(L[1])*int(L[10])*int(L[100])*int(L[1000])*int(L[10000])*int(L[100000])*int(L[1000000])
   


  

