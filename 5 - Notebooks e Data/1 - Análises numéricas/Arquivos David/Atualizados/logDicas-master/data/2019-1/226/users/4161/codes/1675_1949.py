na = int(input("numero apostado: "))
ns = int(input("numero sorteado: "))
a = na//10
b = na - a*10
x = ns//10
y = ns - x*10

if na==ns:
	print("Ganhou R$ 100.000,00")
elif (b*10+a==ns):
	print("Ganhou R$ 50.000,00")
elif (b==x) or (a==x) or (b==y) or (a==y):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")