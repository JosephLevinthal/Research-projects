s = int(input("Qual e a senha? "))

a = (s//100000)%10
b = (s//10000)%10
c = (s//1000)%10
d = (s//100)%10
e = (s//10)%10
f = s%10

c1 = (b + d + f)%(a + c + e)

if(c1 == 0):
	print("acesso liberado")
else:
	print("senha invalida")