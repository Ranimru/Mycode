def isPalindrome(String):
   #this is a method to check whether a string is a Palindrome
   for s in range(0,len(String)//2):
      if String[s]!=String[(len(String)-1)-s]: 
          return False
   return True
print(isPalindrome('foolloof'))
      
