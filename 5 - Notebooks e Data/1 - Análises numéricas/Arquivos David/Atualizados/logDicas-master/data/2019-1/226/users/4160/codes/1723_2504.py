v = int(input("Quantidade inicial de copias do virus no sangue de Micaleteia: "))
l = int(input("Quantidade inicial de leucocitos no sangue: "))
pv = int(input("Percentual de multiplicacao diaria do virus: "))
pl = int(input("Percentual de multiplicacao diaria dos leucocitos: "))

dias = 0 

while(l < 2*v):  
	h = (pv * v/ 100)
	v = v + h
	m = (pl * l/ 100)
	l = l + m
	dias = dias + 1 
print(dias)
	

