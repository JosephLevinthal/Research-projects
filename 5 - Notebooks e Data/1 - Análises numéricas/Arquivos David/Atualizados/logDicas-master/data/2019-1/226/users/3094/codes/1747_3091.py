V = 3
E = 1
D = 0
X = "fim"
r = 0

while(r != X):
	r=input("resultado: ").upper()
	if(r == V):
		re = 3
	elif(r == E):
		re = 1
	elif(r == D):
		re = 0
	else:
		re = 0

p = re * (1/100)
print(p)
		
		
		