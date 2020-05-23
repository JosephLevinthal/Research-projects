p = int(input("Peixes: "))
c = int(input("Fracao: "))
v = int(input("Vendas: "))

# Variavel contadora
anos = 0

# Laco de acumulacao
while (p > 0 and p < 12000):
	p = p + (p*c/100)-v
	anos = anos + 1

if (p <= 0):
	msg = "EXTINCAO"
else:
	msg = "LIMITE"
print(msg)
print(anos)