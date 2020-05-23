a = float(input('NOTA: '))
b = str(input("bonnificacao (S ou N): "))

if b == "S":
	print(a + a*1/10)
else:
	print(a)
