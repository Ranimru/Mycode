List=['SKY','HI','ABC','NONE','A','RANIM','ADHAM']
words=[]
def Trianglenumbers(n):
    TriangleNumbers=[]
    for i in range(1,n):
     t=(i*(i+1)/2)
     TriangleNumbers.append(t)
    return  TriangleNumbers

import string
alpha='#'
alpha=alpha+string.uppercase

for word in List:
 wordindex=[]
 for character in word:
  index=alpha.index(character)
  wordindex.append(index)
 
 for s in Trianglenumbers(1000):
  
  if sum(wordindex)==s:
   words.append(word)

print 'Triangle words are:',words
print 'Number of words=',len(words)
