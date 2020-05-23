pr=float(input("Qual o preco:? "))
pg=float(input("Qual o pagamento:? "))
if (pr > pg):
	print("Falta", pr-pg)
else:
	print("Troco de", pg-pr)