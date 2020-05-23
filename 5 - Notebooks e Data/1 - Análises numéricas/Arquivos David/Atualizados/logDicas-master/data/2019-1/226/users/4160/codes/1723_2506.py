t = int(input("Quantidade inicial de tambaquis no tanque: "))
pt = int(input("Percentual de crescimento anual da quantidade de tambaquis no tanque: "))
v = int(input("Quantidade de tambaquis retirados todos os anos para venda: "))


anos = 0 

while ((t > 0) and (t < 12000)):
	x = (pt * t)/100
	t = t + x - v
	anos = anos + 1
	
if (t < 0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(anos)