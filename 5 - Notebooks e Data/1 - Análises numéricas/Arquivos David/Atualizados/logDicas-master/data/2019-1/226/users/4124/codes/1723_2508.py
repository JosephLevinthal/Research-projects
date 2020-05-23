from math import*
n = int(input("Digite um numero natural: "))
x = 2
i = 1
soma = 0
while(n > i):
	total = ((-1)**(i+1)) * 4/((x)*(x+1)*(x+2))
	soma = soma + total
	#total = 4/((x+2)*(y+2)*(z+2))
	#soma = total + ((-1)**i) * 4/((x+2)*(y+2)*(z+2))
	x = x + 2
	i = i + 1
print(round(3 + soma, 8))
