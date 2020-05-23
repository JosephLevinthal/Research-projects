a = float(input("insira a altura: "))
b = input("sexo M ou F: ").upper()


x = (72.7*a)-58
y = (62.1*a)-44.7

if(b== "F"):
	msg = y
else:
	msg = x

print(round(msg, 2))