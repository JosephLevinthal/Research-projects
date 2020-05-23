qi = int(input("Qtd. inicial: "))
pc = float(input("Percentual de crescimento: "))
qv = int(input("Qtd. para venda: "))
t = 0 #contadora
while (qi > 0 and qi < 12000):
	c = qi * pc / 100
	qi = qi + c - qv
	t = t + 1
if (qi >= 12000):
	print("LIMITE")
elif (qi <= 0):
	print("EXTINCAO")
print(t)
	