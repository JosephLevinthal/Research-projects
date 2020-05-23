qi = int(input("Qtd. inicial: "))
pc = float(input("Percentual de crescimento: "))
t = 0 #contadora
while (qi > 0 and qi < 8000):
	qv = int(input("Qtd. para venda: "))
	c = qi * pc / 100
	qi = qi + c - qv
	t = t + 1
if (qi >= 8000):
	print("MAXIMO")
elif (qi <= 0):
	print("ZERO")
print(t)
	