x=float(input("Altura da torre: "))
y=float(input("Quantidad de metros subindo: "))
z=float(input("Quantidade de metros descendo: "))
g=0
f=1
while(g<x):
	g=g+y
	if(x>g):
	   g=g-z
	   f=f+1
	
print(f)	
	
	