p = int(input("Quantidade inicial de pirarucus no tanque: "))
pp = int(input("Percentual de crescimento mensal da quantidade de pirarucus no tanque: "))

anos = 0 

while ((p > 0) and (p < 8000)):
	m = int(input("A quantidade de pirarucus retirados para venda por mes: "))
	x = (pp * p)/100
	p = p + x - m
	anos = anos + 1

if (p < 0):
	print("ZERO")
else:
	print("MAXIMO")
print(anos)