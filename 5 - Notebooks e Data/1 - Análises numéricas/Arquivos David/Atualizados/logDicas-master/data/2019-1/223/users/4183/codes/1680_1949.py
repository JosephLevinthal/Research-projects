na = int(input("Numero apostado: "))
ns = int(input("Numero sorteado: "))

if (na == ns):
	print("Ganhou R$ 100.000,00")
elif ((na//10)%10 == (ns//10)%10 and (na//1)%10 == (ns//1)%10 or (na//10)%10 == (ns//1)%10 and (na//1)%10 == (ns//10)%10):
	print("Ganhou R$ 50.000,00")
elif ((na//10)%10 == (ns//10)%10 or (na//1)%10 == (ns//1)%10 or (na//10)%10 == (ns//1)%10 or (na//1)%10 == (ns//10)%10):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")