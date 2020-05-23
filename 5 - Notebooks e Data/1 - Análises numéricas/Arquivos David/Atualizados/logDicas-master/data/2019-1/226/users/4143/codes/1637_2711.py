a = float(input("Valor disponivel:"))
b = int(input("Quantos tickets do RU:"))
c = float(input("Valor do tckets:"))
d = int(input("Quantidade de passes no onibus: "))
e = float(input("Valor do passe:"))
eq = (b*c) +  (d*e)
if(a>=eq):
	mgs = "suficiente".upper()
else:
	mgs = "insuficiente".upper()

print(mgs)