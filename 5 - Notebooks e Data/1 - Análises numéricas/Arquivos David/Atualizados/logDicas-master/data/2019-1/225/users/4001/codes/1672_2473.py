ano = int(input("Ano: "))
a = ano % 19
b = ano % 4
c = ano % 7
d = (19*a + 24) % 30
e = (2*b + 4*c + 6*d + 5) % 7

if (ano >= 1900) and (ano <= 2099):
	if (ano != 1954) and (ano != 1981) and (ano != 2049) and (ano != 2076):
		data = (22 +  d + e)
		if (data != 31):
			if (data % 2 == 0):
				data = (22 +  d + e)%31
				mes = (22 +  d + e) % 4 
				print(data, "-", mes, "-", ano)
			else:
				data = (22 +  d + e)%31
				mes = (22 +  d + e) % 4 + 2
				print(data, "-", mes, "-", ano)
		elif (data == 31): 
			data = 22 + 9
			print(data, "- marco -", ano)
	else:
		data = (22 + d + e)%31 - 7
		mes = "abril"
		print(data, "-", mes, "-", ano)
else:
	print("ano invalido")
	