n = int(input("Numero: "))

while(n >= 0):
	exp = len(str(n))
	cont = 1
	n2 = n
	soma = 0
	
	while(cont <= exp):
		e = 10**(exp-cont)
		d1 = n2 // e
		n2 = n2 - (e*d1)
		soma = soma + d1**exp
		cont = cont + 1

	if(soma == n):
		print("ARMSTRONG")
	else:
		print("NAO ARMSTRONG")
		
	n = int(input("Numero: "))