num = int(input("Informe um numero qualquer: \n"))
cont = 1
x = 0
soma = 0

while(cont<num):
	if(num%cont==0):
		x = x + 1
		soma = soma + cont 
		print(cont)
	cont = cont + 1
if(soma == num):
	print("PERFEITO")
else:
	print("NAO PERFEITO")
	
		
