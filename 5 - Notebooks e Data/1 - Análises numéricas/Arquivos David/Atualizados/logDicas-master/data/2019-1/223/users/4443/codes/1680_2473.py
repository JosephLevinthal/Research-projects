ano = int(input("Digite um ano, com quatro digitos: "))

a = ano%19
b = ano%4
c = ano%7
d = (19*a+24)%30
e = (2*b+4*c+6*d+5)%7
if(1900 <= ano <= 2099):
	data = 22 + d + e
	if(ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076):
		if(data > 31):
			data = data-38
			dia = (data)
			print(dia,"-", 4,"-", ano)
		else: 
			print(data+7,"-", 4,"-", ano)
	else:		
		if(data > 31):
			dia = data -31
			print(dia,"-", 4,"-", ano)
		else: 
			print(data,"-", 3,"-", ano)
else:
	print("ano invalido")
	
	                                                                              