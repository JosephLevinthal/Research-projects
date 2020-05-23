from math import*

n = int(input("no. de termos: "))

#valores iniciais
soma = 0 #acumuladora
i = 0    # contadora
fim = n - 1

while(i <= fim):
	soma = soma+ (-1) ** (i)*1/((2*i+1)*3**i)*sqrt(12)
	i = i+1
	
print(round(soma, 8))