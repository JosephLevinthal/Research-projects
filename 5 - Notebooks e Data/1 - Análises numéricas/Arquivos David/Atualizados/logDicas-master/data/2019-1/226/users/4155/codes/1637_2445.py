x = input("escala: ")
v = float(input("valor da temperatura: "))
C = x

if(x.upper() == "C"):
	msg = (v * 9 / 5) + 32
else:
	msg = ((v - 32) / 9) * 5

x = round(msg, 2)
print(x)