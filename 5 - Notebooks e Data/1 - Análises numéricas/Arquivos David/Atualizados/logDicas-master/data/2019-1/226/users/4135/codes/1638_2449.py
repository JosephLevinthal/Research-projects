a = float (input("Digite um numero a de:"))
b = float (input("Digite um numero de b:"))
c = float (input("Digite um numero de c:"))
d = float (input("Digite um numero de d:"))
e = float (input("Digite um numero de e:"))
f = float (input("digite um numero de f:"))
if ((a*e)-(b*d)==0):
	print ("Nao tem solucao")
else:
	x = ((c*e)-b*f)/((a*e)-(b*d))
	y = ((a*f)-(c*d))/((a*e)-(b*d))
print(x)
print(y)