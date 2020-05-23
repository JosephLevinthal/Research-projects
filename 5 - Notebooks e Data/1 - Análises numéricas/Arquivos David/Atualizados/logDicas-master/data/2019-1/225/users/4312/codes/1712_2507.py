qi = int(input("Quant. inicial de pirarucus: "))
pq = float(input("Percentual de cres: "))

i = 0

while(qi > 0 and qi < 8000):
	ven = int(input("Quant. para venda: "))
	x = qi * pq / 100
	qi = qi + x - ven
	i = i + 1
if(qi >= 8000):
	print("MAXIMO")
elif(qi <= 0):
	print("ZERO")
print(i)
	