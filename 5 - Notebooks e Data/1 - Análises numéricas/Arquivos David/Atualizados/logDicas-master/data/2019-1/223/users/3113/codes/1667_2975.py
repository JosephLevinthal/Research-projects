a=int(input("quantidade de sucos:"))
b=int(input("quantidadde de salgados:"))
c=float(input("valor disponivel:"))

f=3.0
s=3.5
p1=a*f
p2=b*s
p3=p1+p2
if(p3<=c):
	
	P=p3
	R="Sim"
else:
	P=p3
	R="Nao"
print(P)
print(R)
	