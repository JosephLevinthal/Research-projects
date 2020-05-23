from math import*
k =int(input("numero natural: ")) 
x = 0
s = 0
fim = k-1
while(x<=fim):
	s = s +1/factorial(x)
	x = x+1 
	
	
	
	
print(round(s ,8))	