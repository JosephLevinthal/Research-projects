n = float(input("digite a nota do aluno: "))
x = input("ele ganhou bonificacao : (S/N)")

X = x.upper()

if X == "S":
	y = n * 0.1
	h = y + n
	print(h)
else:
	print(n)