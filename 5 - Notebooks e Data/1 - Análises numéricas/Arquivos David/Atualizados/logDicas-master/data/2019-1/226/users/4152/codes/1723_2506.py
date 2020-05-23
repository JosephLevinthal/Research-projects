qi = int(input("Quantidade inicial de tambaqui: "))
pc = int(input("Percentual de de crescimento anual dos tambaquis no tanque: "))
qf = int(input("Quantidades de tambaquis retirados todos os anos para venda: "))
a = 0
perc = pc / 100
while (qi > 0) and (qi <= 12000):
	qi = qi + (qi * perc)
	qi = qi - qf
	a = a + 1
if (qi >= 1200):
	t = "LIMITE"
else:
	t = "EXTINCAO"
print(t)
print(a)
		