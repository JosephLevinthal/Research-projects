a = float(input("valor"))
b = int(input("quantidade de tickets do ru"))
c = float(input("valor dos tickets"))
d = int(input("quantidade de passes de onibus"))
e = float(input("valor dos passes"))
if a >= (b*c)+(d*e):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")