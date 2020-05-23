quanInCo = int(input("Quantidade inicial de copias do virus no sangue de Micaleteia:"))
quanInLeu = int(input("Quantidade inicial de leucocitos no sangue:"))
PMultV = int(input("Percentual de multilicacao diaria do virus:"))/100
PMultL = int(input("Percentual de multilicacao diaria dos leucocitos:"))/100

dias = 0
while(quanInCo > quanInLeu/2):
	quanInCo = quanInCo + (quanInCo * PMultV)
	quanInLeu = quanInLeu + (quanInLeu * PMultL)
	dias = dias + 1
print(dias)