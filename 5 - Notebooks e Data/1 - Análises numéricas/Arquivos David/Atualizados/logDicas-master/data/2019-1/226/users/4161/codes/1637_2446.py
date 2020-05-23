senha = int(input("senha: "))
a = senha//100000
b = senha//10000 - (senha//100000)*10
c = senha//1000 - (senha//10000)*10
d = senha//100 - (senha//1000)*10
e = senha//10 - (senha//100)*10
f = senha - (senha//10)*10
c1 = b + d + f
c2 = a + c + e
c1 = max(c1,c2)
c2 = min(c1,c2)
w = int(c1/c2)
v = float(c1/c2)
if (w != v):
	print("senha invalida")
else:
	print("acesso liberado")
