escolha = input("escolha, C or F:")
temp = float(input("valor da temperatura:"))
C1 = (5/9)*(temp - 32)
C2 = (temp * 9/5) + 32
if escolha == "C":
	print(round(C2,2))
else:
	print(round(C1,2))