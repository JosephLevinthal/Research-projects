# Quantidade inicial de pirarucus no tamque
x = int(input("Insira: "))
# Percentual de crescimento mensal da quantidade de pirarucus no tamque
y = int(input("Insira: "))
# Quantidades de pirarucus retiradas por mes

t = 0
while(x > 0 and x < 8000):
	q = int(input("Insira: "))
	r = (x * y) / 100
	x = x + r - q
	t = t + 1
if(x < 0):
	print("ZERO")
else:
	print("MAXIMO")
print(t)