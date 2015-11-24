#creditcard
def check(S):
   if len(S)!=19:
      return False
   T=S.replace(' ','')
   temp=T.isdigit()
   print(temp)
   if temp==False:
      return False
   if S[4]!=' ' or S[9]!=' ' or S[14]!=' ':
      return False
   Sum=0
   for s in T:
      Sum=Sum+int(s)

   if Sum%10!=0:
      return False
   return True
      
#Temp.
def C2F(C):
   F=C*(9/5)+32
   return F
def F2C(F):
   C=(F-32)*(5/9)
   return C

In=input()
t=float(In[0:len(In)-1])
s=In[len(In)-1]
if s=='C':
   Temp=C2F(t)
   Temp=str(Temp)+"F"
if s=='F':
   Temp=F2C(t)
   Temp=str(Temp)+"C"
print(Temp)

