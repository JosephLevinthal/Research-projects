C = input("Insira a escala de temperatura: (C/F)")
val = float(input("Insira o valor da temperatura: "))

if(C.upper() == "C"):
	F = (9/5) * val + 32
	print(F)
else:
	C = (5/9) * (val - 32)
	print(C)