qi = int(input("Quantidade inicial de pirarucus: "))
pc = int(input("Percentual de crescimento: "))
perc = pc / 100
m = 0
while (qi > 0) and (qi <= 8000):
	qf = int(input("Quantidade de pirarucus retirados por mes: "))
	qi = qi + (qi * perc) - qf
	m = m + 1
if (qi > 1200):
	msg = "MAXIMO"
else:
	msg = "ZERO"
print(msg)
print(m)
