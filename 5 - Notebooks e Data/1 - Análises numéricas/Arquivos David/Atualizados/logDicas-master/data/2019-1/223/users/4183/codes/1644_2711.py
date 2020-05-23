a = float(input("Tens "))
b = float(input("Quantos tickests precisas? "))
c = float(input("Valor do ticket: "))
d = float(input("Quantos passes precisas? "))
e = float(input("Valor da passagem: "))
z = b * c + d * e

if (a >= z):
	print("SUFICIENTE")
	
else:
	print("INSUFICIENTE")