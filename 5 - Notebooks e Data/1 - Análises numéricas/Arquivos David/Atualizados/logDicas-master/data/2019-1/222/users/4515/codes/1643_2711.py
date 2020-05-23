valordisponivel=float(input("Informe o valor disponivel :"))

qtdeticket=int(input("Informe quantidade Ticket :"))

valorticket=float(input("Valor do Ticket"))

qtdepasse=int(input("Informe quantidade Passes :"))

valorpasse=float(input("Valor do Ticket"))


valortotal=(qtdeticket*valorticket)+(qtdepasse*valorpasse)

if(valordisponivel >=valortotal):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")

