x=float(input("Valor inicial: "))
y=int(input("Digite a quantidade de meses: "))
h=0
j=x
while(h<y):
	j=j*1.04
	h=h+1
	print(round(j,2))
	
