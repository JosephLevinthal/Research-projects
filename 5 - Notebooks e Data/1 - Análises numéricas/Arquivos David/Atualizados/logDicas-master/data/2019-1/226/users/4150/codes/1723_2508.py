n = int(input("num de aproximacoes; "))

soma = 3 #variavel acumuladora
i = 1    #variavel contadora 
fim = n

while(i<fim):
	soma = soma + ((-1)**(i+1)) * (4/((i*2)*(i*2+1)*(i*2+2)))
	i = i+1 # incremento
	
print(round(soma, 8))