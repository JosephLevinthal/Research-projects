s= float(input("Senha de seis digitos:"))
a=(s//100000)% 10
b=(s//10000)%10
c=(s//1000)%10
d=(s//100)%10
e=(s//10)%10
f=(s//1)%10

if ((b+d+f) % (a+c+e) == 0):
	print("acesso liberado")
else:
	print("senha invalida")