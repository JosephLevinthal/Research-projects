promocao=input("S ou N: ")
ingresso=float(input("valor do ingresso: "))
qntd=float(input("qntd de ingressos: "))
total=ingresso*qntd
promocao=promocao.upper()
if promocao=="S":
	desconto=total-total*0.2
	print(round(desconto,2))
else:
	print(round(total,2))
	