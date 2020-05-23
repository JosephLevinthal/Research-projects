a=float(input("digite um valor: "))
b=float(input("digite um valor: "))
c=float(input("digite um valor: "))
d=float(input("digite um valor: "))
e=float(input("digite um valor: "))
f=float(input("digite um valor: "))
m=(a*e-b*d)
if(m!=0):
	x=(c*e-b*f)/(a*e-b*d)
	y=(a*f-c*d)/(a*e-b*d)
	print(x)
	print(y)
else:
	mensagem="Nao tem solucao"
	print(mensagem)