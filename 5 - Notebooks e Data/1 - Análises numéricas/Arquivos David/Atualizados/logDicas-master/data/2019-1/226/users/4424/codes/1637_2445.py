b = input("Digite um numero: ")
a=float(input("Digite um numero: "))

if (b.upper()=="C"):
	eq=a*(9/5)+32
else:
	eq=(a-32)*(5/9)
	
print(round(eq, 2))