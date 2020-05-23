v=int(input("valor:"))
q=int(input("quantidade de tickets do RU:"))
va=float(input("valor dos tickets:"))
qp=int(input("quantidade de passes de onibus:"))
vp=float(input("valor dos passes:"))

d=va*q
s=(vp*qp)+d
f=v-s
q=v-f

if(v >= q):
	mensagem="SUFICIENTE"
else:
	mensagem="INSUFICIENTE"

print(mensagem.upper())

				