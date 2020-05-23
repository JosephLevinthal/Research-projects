preco = float(input("Qual o preco do produto? "))
pagamento = float(input("Qual o valor que vai pagar? "))

if (preco > pagamento ) :
	x = preco - pagamento 
	print("Falta ", round(x, 2))
else : 
	y = pagamento - preco
	print("Troco de ", round(y, 2))