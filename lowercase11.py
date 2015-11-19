
def lowerChar(char):
   LC=chr(ord(char)+32)
   if ord(char) in range(ord('A'),ord('Z')):
      return LC
   else:
      return char

def lowerString(string):
    result=""
    for s in range(0,len(string)):
       result=result+lowerChar(string[s])
    return result

print(lowerString("tEst arGument"))
   

      


     

