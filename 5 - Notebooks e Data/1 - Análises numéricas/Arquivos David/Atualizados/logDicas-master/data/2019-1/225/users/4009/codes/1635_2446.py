codexu = float(input("codigo: "))

u = (codexu % 10)
x = (codexu / 10) % 10
e = (codexu / 100) % 10
d = (codexu / 1000) % 10
o = (codexu / 10000) % 10
c = (codexu / 100000) % 10

p = c + d + x
s = o + e + u

if s%p == 0:
	print("acesso liberado")
else:
	print("senha invalida")