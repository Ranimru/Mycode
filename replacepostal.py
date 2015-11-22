#replace x by y
def replace(List, X, Y):
   
    counter=0
    for l in List:
         if l==X:
            List.pop(counter)   
            List.insert(counter,Y)
         counter=counter+1

      
      
    print List


replace([2,3,34,2,2],2,7)

#postal code
def postalValidate(S):
   S=S.replace(' ','')

   if len(S)!=6:
      return False
   
   Salpha=S[0]+S[2]+S[4]
   Sdigit=S[1]+S[3]+S[5]
   if not Salpha.isalpha() or not Sdigit.isdigit():
      return False
   
   return S.upper()
