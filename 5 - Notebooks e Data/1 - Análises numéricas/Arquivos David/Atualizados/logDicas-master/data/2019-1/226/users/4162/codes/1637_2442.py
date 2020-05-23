num = int(input("Digite um numero: "))

if (num % 2 == 0):
	mensagem = "Par"
if(num%2 !=0):
	mensagem = "Impar"

print(mensagem.lower())