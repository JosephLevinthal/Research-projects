n = float(input("digite n: "))
soma = 3
i = 1
fim = n
while (i < fim):
	soma = (soma + ((-1)**(i+1))*(4/((i*2)*(i*2+1)*(2*i+2))))
	i = i + 1
	
print(round(soma, 8))