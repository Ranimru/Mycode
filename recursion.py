# count up
def  countup(n):
  if n == 0:
    print('Blastoff!')
    
   
  else:
    countup(n - 1)
    print(n)


#countdown with 2
def countdownBy2(n):
  if n == 0:
     print('Blastoff!')
  if n==1:
     print (n)
     print('Blastoff!')    
  else:
    if n%2!=0 and n<1:
       return n    
    if n%2==0 and n<2:
       return n     
    print(n)
    countdownBy2(n - 2)


#hailstone
def hailstone(n):
      if n==1:
         print(n)
         return n
      if n%2!=0:
         print(n)
         hailstone(3*n+1)
      if n%2==0:
         print(n)
         hailstone(int(n/2))
#digital sum
def digitalSum(n):
  if n < 10:
   return n
  else:
   Sum=n%10+digitalSum(int(n//10))
   return Sum
##
def  digitalRoot(n):
     n=digitalSum(n)
     if n<10:
         return n
     else:
         n=digitalRoot(n) 
         return n
## nested list
def nestedListContains(nL,target):
     if isinstance(nL, int):
        return nL == target

     for i in nL:
         inList = nestedListContains(i,target)
         if inList:
                return inList

     return False


