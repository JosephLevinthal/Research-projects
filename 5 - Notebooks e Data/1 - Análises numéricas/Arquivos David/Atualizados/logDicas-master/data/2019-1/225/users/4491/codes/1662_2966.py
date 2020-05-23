m = input("S ou N: ")
v = float(input("valor: "))
qtd = float(input("quantidade de ingresso: "))

if(m == "S"):
	d = (v*qtd) - (v*qtd*20/100)
	print(round(d, 2))
else: 
	p = v*qtd
	print(round(p, 2))