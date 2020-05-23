valor_aluno = float(input("v: "))
qtd_ticket = int(input("qtd: "))
valor_ticket = float(input("v2: "))
qtd_passe = int(input("qtd2: "))
valor_passe = float(input("v3: "))

if (valor_aluno > 300):
	mensagem = "SUFICIENTE"
else: 
	mensagem = "INSUFICIENTE"

print(mensagem)