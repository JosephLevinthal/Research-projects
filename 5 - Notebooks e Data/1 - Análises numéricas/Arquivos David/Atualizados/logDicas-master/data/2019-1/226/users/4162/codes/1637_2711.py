vl= float(input("insira o valor disponivel: "))
qru= int(input("insira a  quantidade de fichas do RU: "))
vlt= float(input("insira o preco do ticket: "))
qp=  int(input("insira a quantidade de passes: "))
vqp= float(input("insira o valor do passe: "))
t=qru*vlt+qp*vqp

if vl>=t:
	print("SUFICIENTE")
if vl<t:
	print("INSUFICIENTE")






