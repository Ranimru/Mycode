L=[0,1]
for i in range(2,2000000):
    for j in str(i):
        L.append(j)

print int(L[1])*int(L[10])*int(L[100])*int(L[1000])*int(L[10000])*int(L[100000])*int(L[1000000])
    
