qi = int(input("Quantidade inicial de peixes: "))
pc = float(input("Percentual de crescimento da qi: "))/100
m = 0
while(qi >= 0 and qi <= 8000):
	pr = int(input("Pirarucus retirados para venda: "))
	qi = qi + (qi * pc) - pr
	m = m + 1
if(qi <= 0):
	print("ZERO")
elif(qi >= 8000):
	print("MAXIMO")
print(m)