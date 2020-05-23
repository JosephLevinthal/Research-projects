qi = int(input("Q inicial: "))
pc = float(input("Percentual de crescimento: "))
t = 0
while (qi > 0 and qi < 8000):
	qv = int(input("Q para venda: "))
	c = qi * pc / 100
	qi = qi + c - qv
	t = t + 1
if (qi >= 8000):
	print("MAXIMO")
elif (qi <= 0):
	print("ZERO")
print(t)