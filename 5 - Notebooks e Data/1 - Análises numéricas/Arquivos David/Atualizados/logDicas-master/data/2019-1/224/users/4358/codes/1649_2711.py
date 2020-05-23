vr1=float(input("Digite a valordispoivel:"))
vr2=int(input("Digite a quantidade de tickets do RU:"))
vr3=float(input("Digite o valor dos tickets:"))
vr4=int(input("Digite a quantidade de passes de onibus:"))
vr5=float(input("Digite o valor dos passes:"))
custo=(vr2*vr3)+(vr4*vr5)
if(vr1>custo):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")