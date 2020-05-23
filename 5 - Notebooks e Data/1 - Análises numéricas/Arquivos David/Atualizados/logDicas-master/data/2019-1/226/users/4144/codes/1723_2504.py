a = int(input("Quantidade inicial de copias do virus no sangue de Micaleteia: "))
b = int(input("Quantidade inicial de leucocitos no sangue: "))
c = float(input("Percentual de multiplicacao diaria do virus: "))
d = float(input("Percentual de multiplicacao diaria dos leucocitos: "))
k = 0
while(b<2*a):
	cpa= (a*c)/100
	cpb= (b*d)/100
	a = a + cpa
	b = b + cpb
	k = k+1
print(k)