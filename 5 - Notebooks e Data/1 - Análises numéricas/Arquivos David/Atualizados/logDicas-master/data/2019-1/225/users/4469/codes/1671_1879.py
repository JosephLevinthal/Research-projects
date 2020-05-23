# Ao testar sua solução, não se limite ao caso de exemplo.
he = float(input())
hf = float(input())

print(str(he) + " extras e " + str(hf) + " de falta")

h  = (he) - ((1 / 4) * (hf))

if(h > 400.0):
	print("R$ 500.0")
else:
	print("R$ 100.0")