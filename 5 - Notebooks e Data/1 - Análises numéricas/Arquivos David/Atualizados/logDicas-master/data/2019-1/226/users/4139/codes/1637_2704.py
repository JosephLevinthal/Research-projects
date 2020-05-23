n = float(input("nota do aluno:"))
b = input("bonificacao S ou N?:")
b = b.upper()
if (b == "S"):
	a = (n+(n*0.1))
else:
	a = n

print(a)