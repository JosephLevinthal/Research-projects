a = float(input("Nota aulo:"))
b = input("Aluno recebera a bonificacao:")
eq = (10/100)*a
if (b.upper() == "S"):
	
	eq2 = a + eq
else:
	eq2 = a
print(eq2)