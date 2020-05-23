pt= float(input("insira o preco total: "))
a=pt-(pt*0.05)
if pt>=200:
	print(round(a,2))
else:
	print(pt)