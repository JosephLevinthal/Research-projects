temp1 = input("Digite valor: ")
temp2 = float(input("Digite valor: "))

if(temp1 == "F"):
	formula  = ((5/9)*(temp2 - 32))

else:
	formula = ((temp2*(9/5))+32)
print(round(formula, 2))
	
	