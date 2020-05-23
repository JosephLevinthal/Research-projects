cash = float(input("Quanto dinheiro o aluno tem? "))
ru = int(input("Qual a quantidade de RU que desejas? "))
cru = float(input("Qual o custo do ru?"))
passe = int(input("Quantos passes de onibus desejas? "))
cpasse = float(input("Qual o valor dos passes? "))

gasto = ru*cru + passe*cpasse

if(cash >= gasto):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
