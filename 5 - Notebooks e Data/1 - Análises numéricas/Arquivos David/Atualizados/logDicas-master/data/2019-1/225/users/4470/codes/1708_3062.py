q=int(input("quantidade de pecas de ouro:"))
n=input("nome da arma:")
f=int(input("fator de sucesso:"))
d=q*f
if(1>f)or(f>10):
	print("Entrada invalida")
elif(q=="ESPADA")and(n==1<f<10):
	x=d*10
	print(x)
elif(q=="MACHADO")and(n==1<f<10):
	x=d+3
	print(x)
elif(n=="MARRETA")and(n==1<f<10):
	x=d+5
	print(x)
else:
	print("PO insuficiente")