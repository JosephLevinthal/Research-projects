p=float(input("Digite o percurso em quilometros: "))
t=input("Digite carro A ou B: ")
if(t.upper()=="A"):
   x=p/8
else:
	x=p/12
print(round(x,2))	

	