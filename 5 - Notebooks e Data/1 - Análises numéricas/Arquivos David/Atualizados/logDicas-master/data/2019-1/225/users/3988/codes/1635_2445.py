T = input("temperatura (C/F):")
V = float(input("valor:"))
Cs = (5/9) * (V - 32)
Fh = ((9 * V) / 5 + 32)
if (T == "C"):
	msg = Fh
else:
	msg = Cs
print(round(msg, 2))	