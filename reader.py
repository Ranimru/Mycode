#poet analysis
def reader():
    L = []
    while True:
        line = input()
        if line.endswith("###"):
           return L 
        Lower=line.lower()
        L.extend(Lower.split())
                 
o=reader()
print o

Counts=[]
for s in o:
     count=o.count(s)
     Counts.append(count)

print Counts

Max=max(Counts)
print Max
place=Counts.index(Max)
word=o[place]

print(word)
