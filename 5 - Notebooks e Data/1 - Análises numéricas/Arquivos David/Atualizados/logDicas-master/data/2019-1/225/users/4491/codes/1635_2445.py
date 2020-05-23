T = input("C ou F: ")
V = float(input("valor da temperatura: "))
C = (5 * V - 5 *32)/9
F = ((9*V/5) + 32)

if(T == "C"):
	print(round(F, 2))
else: 
	print(round(C, 2))