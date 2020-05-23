#Entradas
V=int(input("Insira o valor disponivel:"))
#Entrada do RU
t=int(input("Insira a quantidade desejada:"))
Vt=float(input("Insira o valor dos tickets:"))
#Entradas do passe 
Qp=int(input("Insira a quantidade de passes desejado:"))
Vp=float(input("Insira o valor dos passes"))

if(Vt*t + Qp*Vp < V):
	msg= "suficiente"
else:
	msg= "insuficiente"

print(msg.upper())