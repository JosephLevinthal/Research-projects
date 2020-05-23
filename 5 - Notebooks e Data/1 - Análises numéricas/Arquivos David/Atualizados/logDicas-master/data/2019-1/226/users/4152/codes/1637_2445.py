esc = input("Digite aqui a escala da temperatura: ")

T = float(input("Digite aqui a temperatura: "))

c = (5 / 9) * (T - 32)

f = T * (9 / 5) + 32

if(esc.upper() == "F"):
	msg = c
if(esc.upper() == "C"):
	msg = f
	
print(round(msg, 2))

