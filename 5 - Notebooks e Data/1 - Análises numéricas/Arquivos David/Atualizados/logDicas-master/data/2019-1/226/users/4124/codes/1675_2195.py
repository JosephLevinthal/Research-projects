num = int(input("Digite a data: "))
d = num // 1000000
d1 = num % 1000000
m = d1 // 10000
m1 = d1 % 10000
a = m1

if(a > 0 and m >= 1 and m <= 12 and d >= 1):
	if(a % 4 == 0):
		if(m == 2):
			if(d > 29):
				print(d," de fevereiro de", a, "nao eh uma data valida")
			else:
				print(d," de fevereiro de", a, "eh uma data valida")
	elif(a == 1582):
		if((d >= 5 and m == 10) or (d <= 14 and m == 10)):
			print(d," de outubro de ", a, " nao eh uma data valida")
		else:
			print(d," de ", m," de ", a, "eh uma data valida")
	else:
		print(d," de ", m," de ", a, "eh uma data valida")
else:
	print(d," de ", m," de ", a, "nao eh uma data valida")
			
			
			