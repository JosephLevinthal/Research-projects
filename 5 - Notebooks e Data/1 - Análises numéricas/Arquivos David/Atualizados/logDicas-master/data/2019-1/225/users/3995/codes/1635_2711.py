t=float(input("valor disponivel:"))
q=int(input("quantidade de tickets:"))
v=float(input("preco dos tickets:"))
p=int(input("quantidade de passes:"))
j=float(input("preco dos passes:"))
h=float((q*v)+(p*j))
if(t>=h):
	msg=("SUFICIENTE")
else:
	msg=("INSUFICIENTE")
print(msg)