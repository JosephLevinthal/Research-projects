q=float(input("Quantidade de peca de ouro:"))
n=input(" Nome da arma ( ESPADA, MACHADO ou MARRETA)")
d=float(input(" Fator do sucesso ( Entre 1 a 10):"))
if(q < 30):
	print("PO insuficiente")
elif(d<1 or d>10):
	print("Entrada invalida")
elif(q>=100):
	f=d*10
elif(q>=30):
	f=d+3
elif(q>=50):
	f=d+5
print(f)	
print(n)
print(d)
