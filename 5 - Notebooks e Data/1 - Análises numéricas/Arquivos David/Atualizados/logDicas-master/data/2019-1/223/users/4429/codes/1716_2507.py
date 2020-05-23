p = int(input("Peixes: "))
c = int(input("Fracao: "))


# Variavel contadora
meses = 0

# Laco de acumulacao
while (p > 0 and p < 8000):
	v = int(input("Vendas: "))
	p = p + (p*c/100)-v
	meses = meses + 1
	

if (p <= 0):
	msg = "ZERO"
else:
	msg = "MAXIMO"
print(msg)
print(meses)
