n = int(input("numero: "))

while (n>=0):
	expoente = len(str(n))
	cont = 1
	number = n
	soma = 0
	
	while (cont <= exp):
		e = 10**(expoente-cont)
		d1 = number // e
		number = number - (e*d1)
		soma = soma + d1**exp
		cont = cont + 1
	if (soma == n):
		print("ARMSTRONG")
	else:
		print("NAO ARMSTRONG")
	n = int(input("Numero: "))

	
