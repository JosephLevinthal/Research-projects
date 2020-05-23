a = int(input("digite numero 1: "))
b = int(input("digite numero 2: "))

produto = a*b
formula = produto%2

if(formula==0):
	mensagem = a+b
else:
	mensagem = b-a

print(mensagem)