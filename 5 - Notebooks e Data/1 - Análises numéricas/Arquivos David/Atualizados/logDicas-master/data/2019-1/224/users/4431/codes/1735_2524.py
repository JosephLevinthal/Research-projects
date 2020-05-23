from math import*
x=int(input("Digite um numero inteiro: "))
g=3
z=0
while(x>g):
	g=g+1
	if(g%2==0):
		print(g)	
		z=(sin((pi/g)))/(sin((2*pi)/g))
		print(round(z,4))
	else:
		print(g)
		f=(sin(pi/g))/(sin((3*pi)/(2*g)))
		print(round(f,4))
		
		
		
		
	
   