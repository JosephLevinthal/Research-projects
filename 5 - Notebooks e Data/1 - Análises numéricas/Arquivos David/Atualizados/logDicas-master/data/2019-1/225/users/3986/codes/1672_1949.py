na=int(input("numero apostado de dois digitos:"))
ns=int(input("numero sorteado de dois digitos:"))
a1=na//10
a2=na%10
s1=ns//10
s2=ns%10
if a1==s1 and a2==s2:
	print("Ganhou R$ 100.000,00")
elif a1==s2 and a2==s1:
	print("Ganhou R$ 50.000,00")
elif a1==s1 or a1==s2 or a2==s1 or a2==s2:
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")