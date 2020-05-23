numero = int(input("Digite a senha: "))

a = numero // 100000

b = (numero % 100000) // 10000

c = ((numero % 100000) % 10000) // 1000

d = (((numero % 100000) % 10000) % 1000)//100

e = ((((numero % 100000) % 10000) % 1000)%100)//10

f = (((((numero % 100000) % 10000) % 1000)%100)%10)

x = b + d + f
y = a + c + e

if(x%y == 0):
	print("acesso liberado")
else:
	print("senha invalida")