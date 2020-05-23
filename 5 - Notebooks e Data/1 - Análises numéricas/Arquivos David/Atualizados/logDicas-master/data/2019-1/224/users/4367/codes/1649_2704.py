nota=float(input("digite um numero de 0 a 10: "))
boni=input("escolha S ou N: ")
if(boni.upper()=="S"):
	nota_final= nota+nota*10/100
else:
	nota_final= nota
print(nota_final)