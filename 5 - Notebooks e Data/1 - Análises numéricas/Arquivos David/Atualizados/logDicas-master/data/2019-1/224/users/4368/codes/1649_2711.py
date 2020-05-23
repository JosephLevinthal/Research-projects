valor=float(input())
quantidade_de_tickets=int(input())
valor_tickets=float(input())
quantidade_de_passes_de_onibus=int(input())
valor_passes=float(input())

if valor < ((quantidade_de_tickets*valor_tickets)+(quantidade_de_passes_de_onibus*valor_passes)):
	print("INSUFICIENTE")

else:
	print("SUFICIENTE")

