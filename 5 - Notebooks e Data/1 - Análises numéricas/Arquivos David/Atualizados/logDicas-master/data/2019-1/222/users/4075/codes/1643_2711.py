valor=float(input("leia o valor:"))
a=int(input("leia a quantidade de tickets do RU:"))
b=float(input("leia o valor dos tickets:"))
c=int(input("leia a quantidade de passes de onibus:"))
d=float(input("leia o valor dos passe:"))
soma= (a*b)+(c*d)

if(valor>=soma):
	mensagem="SUFICIENTE"
else:
	mensagem="INSUFICIENTE"

print(mensagem.upper())
