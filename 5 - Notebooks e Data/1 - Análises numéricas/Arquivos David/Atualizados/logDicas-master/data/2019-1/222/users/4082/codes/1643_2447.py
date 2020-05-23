preco = float(input())
pagamento = float(input())

f = preco - pagamento
t = pagamento - preco

falta = round(f,2)
troco = round(t,2)

if( preco > pagamento):
	print('Falta',falta)

elif (preco <= pagamento):
	print('Troco de',troco)