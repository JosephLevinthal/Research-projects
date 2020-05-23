p = float(input("nota: "))
bn = input("bonificacao(S/N):")
if(bn.upper()=="S"):
	print(p+(p*0.10))
else:
	print(p)