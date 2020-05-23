a=float(input("digite o numero"))
b=float(input("digite o numero"))
c=float(input("digite o numero"))
d=float(input("digite o numero"))
e=float(input("digite o numero"))
f=float(input("digite o numero"))
x=(c*e-b*f/a*e-b*d)
y=(a*f-c*d/a*e-b*d)
if (a*e-b*d!=0):
	mensagem= "Tem soluçao "
else:
	mensagem="Nao tem soluçao"
print(x,y)