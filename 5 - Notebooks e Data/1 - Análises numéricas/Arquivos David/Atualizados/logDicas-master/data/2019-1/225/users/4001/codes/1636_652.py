# Entrada
n = int(input("n: "))
# Condicao

if (n % (n % 100) == 0):
	msg = "SIM"
else:
	msg = "NAO"
print(msg)