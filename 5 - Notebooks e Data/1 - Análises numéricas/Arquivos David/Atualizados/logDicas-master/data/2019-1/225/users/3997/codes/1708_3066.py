qi = int(input("quantidade de pts inicial: "))
d1 = int(input("Digite um nmr: "))
d2 = int(input("Digite um nmr: "))
d3 = int(input("Digite um nmr: "))


N = d1 + d2 + d3
qr = qi - (10*N)
print(int(qr))

if(qr>0):
	print("VIVO")
elif(qr == 0):
	print("MORTO")
elif (qi<0 or 1>d1<12 and 1>d2<12 and 1>d3<12):
	print("Entrada invalida")
