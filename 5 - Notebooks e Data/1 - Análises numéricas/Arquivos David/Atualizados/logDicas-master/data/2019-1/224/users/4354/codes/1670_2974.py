qte_acai = float(input("quantidade do acai: "))
qte_salgados = float(input("quantidade de salgados: "))
valor_pago = float(input("valor pago: "))
acai = qte_acai * 0.024
salgado = 3 * qte_salgados
if(valor_pago == acai + salgado) :
	print(round(acai+salgado,2))
	print("Nao")
if(valor_pago > acai + salgado) :
	troco = valor_pago -(acai + salgado)
	print(round(acai+salgado,2))
	print("Sim")