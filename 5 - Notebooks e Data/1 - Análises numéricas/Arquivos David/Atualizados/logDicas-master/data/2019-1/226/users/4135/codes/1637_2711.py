valor = float (input("Digite o valor disponivel:"))
qtd_tickets = int (input("Digite a quantidade de tickets que deseja comprar:"))
valor_tickets = float (input("Digite o valor dos tickets:"))
qtd_passes = int (input("Digite a quantidade de passes para comprar:"))
valor_passe = float (input("Digite o valor dos passes:"))
if ((qtd_tickets*valor_tickets+qtd_passes*valor_passe)<=valor):
	print ("suficiente".upper())
else:
	print ("insuficiente".upper())
