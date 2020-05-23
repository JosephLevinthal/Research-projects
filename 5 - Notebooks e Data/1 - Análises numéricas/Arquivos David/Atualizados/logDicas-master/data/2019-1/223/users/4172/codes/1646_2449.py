a=float(input("conjunto: "))
b=float(input("conjunto: "))
c=float(input("conjunto: "))
d=float(input("conjunto: "))
e=float(input("conjunto: "))
f=float(input("conjunto: "))

x=((c*e)-(b*f))/((a*e)-(b*d))
y=((a*f)-(c*d))/((a*e)-(b*d))

if x==0 :
	x=((c*e)-(b*f))/((a*e)-(b*d))
	mensagem=(x)
	y=((a*f)-(c*d))/((a*e)-(b*d))
	me1=(y)
else:
	mensagem="Nao tem solucao"
   me1="Nao tem solucao"

print(mensagem)
print(me1)