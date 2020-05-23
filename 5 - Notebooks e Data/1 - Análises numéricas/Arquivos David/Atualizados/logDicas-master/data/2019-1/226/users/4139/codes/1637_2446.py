a = int(input("digite a senha:"))

x = a // 100000
y = a // 10000%10
z = a // 1000%10
i = a // 100%10
j = a // 10 % 10
k = a % 10

s = x + z + j
ss = y + i + k

if(ss%s==0):
	print("acesso liberado")
else:
	print("senha invalida")