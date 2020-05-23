p= float(input("insira o percurso da viagem: "))
t= input("insira o tipo de carro A/B: ")
if t.upper()=="A":
	c=8
if t.upper()=="B":
	c=12
print (round(p/c,2))