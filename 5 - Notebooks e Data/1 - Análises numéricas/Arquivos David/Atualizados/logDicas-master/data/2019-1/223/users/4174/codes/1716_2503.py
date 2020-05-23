n = int(input("numero natural de n:"))
pi = 0 

while (n >= 1):
	if ( n%2 == 1):
		pi = pi + (4/(2*n-1)) 
	else:
		pi = pi - (4/(2*n-1))
		
	n = n-1
print(round(pi,8))		
	

