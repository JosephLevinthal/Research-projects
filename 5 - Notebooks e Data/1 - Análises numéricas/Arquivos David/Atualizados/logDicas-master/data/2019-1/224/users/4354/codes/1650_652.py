numero = int(input("digite o numero: "))
if(numero >= 100 and numero <= 999) :
	d1 = numero // 100
	d2 = (numero % 100) // 10
	d3 = numero % 100
	if(numero % d3 == 0) :
		print("SIM")
	else :
		print("NAO")		
	
	
	