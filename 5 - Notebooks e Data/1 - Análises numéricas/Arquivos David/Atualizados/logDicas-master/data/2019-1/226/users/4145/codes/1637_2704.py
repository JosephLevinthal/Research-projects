n = float(input("nota de zero a dez: "))
b = input(" receber bonificacao: ")

if (b == "S"):
	nf = n + ((10/100)*n)
else:
	nf = n
	
print(nf)