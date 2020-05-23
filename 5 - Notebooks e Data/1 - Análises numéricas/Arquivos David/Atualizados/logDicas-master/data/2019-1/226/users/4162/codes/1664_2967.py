a1= float(input("insira sua altura: "))
a2= float(input("insira a altura do amigo: "))
if a1>=1.37 or a2>=1.37:
	print("Sim")
	print(max(a1,a2))
if a1<1.37 and a2<1.37:
	print("Nao")
	print(max(a1,a2))