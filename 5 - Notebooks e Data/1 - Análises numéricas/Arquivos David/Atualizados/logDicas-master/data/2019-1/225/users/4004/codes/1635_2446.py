codigu = int(input("senha:{1,6} "))

u = (codigu % 10)
g = (codigu // 10) % 10
i = (codigu // (10 ** 2)) % 10
d = (codigu // (10 ** 3)) % 10
o = (codigu // (10 ** 4)) % 10
c = (codigu // (10 ** 5)) % 10

cdg = c + d + g
oiu = o + i + u
r = oiu % cdg

if r == 0:
	print("acesso liberado")
else:
	print("senha invalida")