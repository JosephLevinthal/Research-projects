s = int(input("Digite a senha: "))
a = s // 100000
b = (s // 10000) %10
c = (s // 1000)%10
d = (s // 100)%10
e = (s //10)%10
f = s % 10
x = b + d + f
y = a + c + e
h = x%y
if (h == 0):
	print("acesso liberado")
else:
	print("senha invalida")
	