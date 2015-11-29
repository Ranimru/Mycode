#10--(3,5)--3,5,6,9
#problem 1
def multiples():
	L=[]
	for x in range(1,1000):
	    if x%3==0 or x%5==0:
	     L.append(x)

	    
	print sum(L)     

#problem 2
def Fibonacci():
        sequence = [0, 1, 1]
        i=3
        Sum=0
        while(True):  
             value=sequence[i-1] + sequence[i-2]
             if value>4000000:
                 return Sum 
             if value%2==0:
                 Sum=Sum+value
            
             sequence.append(value)
             i=i+1
        return Sum

print Fibonacci()


