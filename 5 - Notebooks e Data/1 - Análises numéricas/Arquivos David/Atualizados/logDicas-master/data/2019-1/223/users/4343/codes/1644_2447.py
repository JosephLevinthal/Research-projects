preco = float (input("Qual o preco da sua compra?"))
pagamento = float(input("Quanto voce pagou?"))

if(preco>pagamento):
	mensagem = "Falta " + srt (pagamento-preco)
else:
	mensagem = "Troco de " + srt (pagamento-preco)
 print(mensagem)