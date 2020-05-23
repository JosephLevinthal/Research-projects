senha = int(input("senha: "))
a = senha // 100000
a1 = senha % 100000
b = a1 // 10000
b1 = a1 % 10000
c = b1 // 1000
c1 = b1 % 1000
d = c1 // 100
d1 = c1 % 100
e = d1 // 10
e1 = d1 % 10
f = e1
#print(a,b,c,d,e,f)
#x = b + d + f
if((b + d + f) % (a + c + e) == 0):
	print("acesso liberado")
else:
	print("senha invalida")