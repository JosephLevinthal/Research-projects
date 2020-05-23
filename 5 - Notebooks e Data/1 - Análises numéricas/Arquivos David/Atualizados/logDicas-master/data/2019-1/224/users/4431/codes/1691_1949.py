x=int(input("Digite o numero apostado: "))
y=int(input("Digite o numero sorteado: "))
t=x//10
p=x%10
q=y//10
g=y%10
if(x==y):
	print("Ganhou R$ 100.000,00")
elif(t==g)and(p==q):
	print("Ganhou R$ 50.000,00")
elif(t==q)or(t==g)or(p==q)or(p==g):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")