x=float(input("Digite um numero: "))
j=1
g=0
while(j<=x):
	if(x%j==0):
		print(j)
		j=j+1
		g=g+1
	else:
		j=j+1

if(g==1):
	print("1 divisor")
else:
	print(g,"divisores")