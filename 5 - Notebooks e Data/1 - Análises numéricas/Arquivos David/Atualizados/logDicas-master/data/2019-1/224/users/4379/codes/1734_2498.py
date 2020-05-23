na=int(input("digite o numero de habitantes de A"))
nb=int(input("digite o numero de habitantes de B"))
pa=float(input(" percentual de A"))
pb=float(input(" percentual de B"))
t=0
while(na<nb):
	na=na+na*pa/100
	nb=nb+nb*pb/100
	t=t+1
print(t)

