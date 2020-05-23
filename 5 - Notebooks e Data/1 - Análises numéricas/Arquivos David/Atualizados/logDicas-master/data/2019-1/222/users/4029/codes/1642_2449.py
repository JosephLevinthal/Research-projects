a= int(input("Digite o coef. 'a': "))
b= int(input("Digite o coef. 'b': "))
c= int(input("Digite o coef. 'c': "))
d= int(input("Digite o coef. 'd': "))
e= int(input("Digite o coef. 'e': "))
f= int(input("Digite o coef. 'f': "))
h= ((a*e)-(b*d))
x= ((c*e)-(b*f)) / h
y= ((a*f)-(c*d)) / h
if (h == 0): 
	print("Nao tem solucao")
else:
	print(x)
	print(y)