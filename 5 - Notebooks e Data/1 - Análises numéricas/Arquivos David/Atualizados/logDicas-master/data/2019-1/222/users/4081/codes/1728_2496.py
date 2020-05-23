cont=0
soma=0
num=int(input("numero:"))
while(num != -1):
	
	soma = soma + num 
	cont = cont + 1 
	num = int(input("digite o numero: "))
	
if(cont>0):
	print(round(soma,2))