# Quantidade inicial de cópias do vírus no sangue de Micaleteia.
v = int(input("Digite a quantidade inicial de copias do virus no sangue de Micaleteia: "))
l = int(input("Digite a quantidade inicial de leucocitos no sangue: "))
pv = float(input("Percentual de multiplicacao diaria do virus: "))
pl = float(input("Percentual de multiplicacao diaria dos leucocitos: "))

dia = 0 

while(l < 2*v):
	v = v + (v*(pv/100))
	l = l + (l*(pl/100))
	dia = dia + 1

print(dia)
		  