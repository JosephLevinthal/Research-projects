esc = input("Em que escala voce quer a temperatura:")
vlt = float(input("Valor da temperatura:"))

ftc = (vlt - 32)*(5/9)
ctf = (vlt*9/5) + 32

if (esc.upper() == "C"):
	msg = ctf
else:
	msg = ftc

print(round(msg, 2))	