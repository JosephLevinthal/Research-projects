na = int(input("Numero da aposta:"))
ns = int(input("Numero sorteado:"))

a ="Ganhou R$ 100.000,00"
b ="Ganhou R$ 50.000,00"
c ="Ganhou R$ 1.000,00"

x = na//10
y = na%10

z = ns//10
w = ns%10


if(na==ns):
	print(a)
elif(x==w)and(y==z):
	print(b)
elif(x==w) or (x==z) or (y==w) or (y==z):
	print(c)
else:
	print("Perdeu")