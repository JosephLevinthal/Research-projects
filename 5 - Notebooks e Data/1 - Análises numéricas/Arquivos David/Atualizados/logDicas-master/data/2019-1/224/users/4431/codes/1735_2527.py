x=float(input("Digite um numero: "))
j=1
g=0
while(j<x):
	if(x%j==0):
		print(j)
		g=j+g
		j=j+1
		
	else:
		j=j+1

if(g==x):
	print("PERFEITO")
else:
	print("NAO PERFEITO")