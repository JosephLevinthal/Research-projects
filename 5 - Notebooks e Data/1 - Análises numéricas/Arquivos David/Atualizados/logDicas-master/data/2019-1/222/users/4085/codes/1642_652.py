a = int(input("escreva um numero de 3 digitos: "))
b = a // 100 
b1 = a % 100 
c = b1 // 10
c1 = b1 % 10 
d = c1 // 1
num = a - (b * 100)
if (a % num == 0):
	mensagem = "SIM"
else: 
	mensagem = "NAO"
print(mensagem)
