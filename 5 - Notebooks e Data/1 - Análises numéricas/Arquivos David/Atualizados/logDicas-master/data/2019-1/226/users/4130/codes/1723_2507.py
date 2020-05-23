p = int(input("Quantidade inicial de pirarucus: "))
pc = int(input("Percentual de crescimento: ")) / 100

m = 0

while(p > 0 and p < 8000):
	pr = int(input("Quantidade de pirarucus retirados: "))
	p = p + p * pc - pr
	m = m + 1
if(p <= 0):
	print("ZERO")
else:
	print("MAXIMO")
print(m)