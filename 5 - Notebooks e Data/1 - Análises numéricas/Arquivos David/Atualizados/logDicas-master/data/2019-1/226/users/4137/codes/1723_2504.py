qtv = int(input("Quantidade inicial de virus:"))
qtl = int(input("Quantidade inicial de leucocitos:"))
pv = int(input("Percentual da multiplicacao diaria do virus:"))/100
pl = int(input("Percentual da multiplicacao diaria dos leucocitos:"))/100


dia = 0
virus = qtv
leo = qtl


while(leo<virus*2):
	virus = virus * pv + virus
	leo = leo * pl + leo
	dia = dia + 1
print(dia)