S0 = int(input("espaco inicial: "))
v = int(input("velocidade: "))
t = int(input("tempo: "))

S = S0 + (v * t)

print(S)
if v > 100:
	print("ACIMA")
else:
	print("OK")