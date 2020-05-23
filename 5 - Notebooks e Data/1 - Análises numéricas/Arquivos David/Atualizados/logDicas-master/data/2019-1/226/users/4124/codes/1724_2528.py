soma = 0
d = 0
x = 1
while(x > 0):
	x = int(input("Digite um numero positivo: "))
	d = d + 1
	soma = soma + x ** d
	if(soma == x):
		print("ARMSTRONG")
	else:
		print("NAO ARMSTRONG")
	
	