t=input()
valor = float(input())

if(t == 'C'):
	f = (9*valor)/5 + 32
	print(round(f,2))
	
if(t == 'F'):
	c= (5/9)*(valor-32)
	print(round(c,2))

