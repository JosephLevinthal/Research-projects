num = int(input("Digite a senha: "))

digito_1 = num//100000
digito_2 = (num//10000)%10
digito_3 = (num//1000)%10
digito_4 = (num//100)%10
digito_5 = (num//10)%10
digito_6 = num%10

if((digito_2 + digito_4 + digito_6) % (digito_1 + digito_3 + digito_5) !=0):
	mensagem = "senha invalida"
else: 
	mensagem = "acesso liberado"

print(mensagem)
