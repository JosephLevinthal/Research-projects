valor= float(input("quantia:"))
tickets= int(input("quantidade:"))
preco= float(input("tickets:"))
onibus= int(input("quantidade"))
passe= float(input("valor"))
total= (tickets * preco) + (onibus * passe)

if(valor > total):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")