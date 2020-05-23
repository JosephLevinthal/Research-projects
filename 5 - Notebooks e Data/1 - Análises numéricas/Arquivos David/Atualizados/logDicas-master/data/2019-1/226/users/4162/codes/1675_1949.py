na= int(input("digite numero apostado pelo jogador: "))
ns= int(input("digite numero sorteado na loteria: "))
na2=(na%10)
na1=(na//10)
ns2=(ns%10)
ns1=(ns//10)
if (na==ns):
	print("Ganhou R$ 100.000,00")
elif (na1==ns2)and(na2==ns1):
	print("Ganhou R$ 50.000,00")
elif (na1==ns1)or(na1==ns2)or(na2==ns1)or(na2==ns2):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")
