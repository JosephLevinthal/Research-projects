qic = int(input("Quantidade inicial de copias do virus no sangue de Micaleteia: "))
qil = int(input("Quantidade inicial de leucocitos no sangue: "))
pmdv = float(input("Percentual de multiplicacao diaria do virus: "))
pmdl = float(input("Percentual de multiplicacao diaria dos leucocitos: "))
pmdv=pmdv/100
pmdl=pmdl/100
cont=0
while(qil/qic)<=2:
	qil=qil*pmdl+qil
	qic=qic*pmdv+qic
	cont+=1
print(cont)