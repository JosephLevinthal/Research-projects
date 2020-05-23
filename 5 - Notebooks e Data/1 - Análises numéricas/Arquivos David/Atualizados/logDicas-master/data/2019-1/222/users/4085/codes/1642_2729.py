num1 = int(input("escreva um numero inteiro: "))
num2 = int(input("escreva um numero inteiro: "))
if (num1 * num2 % 2 == 0):
	mensagem = num1 + num2
else:
	mensagem = num2 - num1
print(mensagem)