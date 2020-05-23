senha = int(input())
a1 = senha // 100000
r1 = senha % 100000
a2 = r1 // 10000
r2 = r1 % 10000
a3 = r2 // 1000
r3 = r2 % 1000
a4 = r3 // 100
r4 = r3 % 100
a5 = r4 // 10
a6 = r4 % 10
if ((a2 + a4 + a6) % (a1 + a3 + a5) ==0):
	print ("acesso liberado")
else:
	print("senha invalida")