a = input("digite uma letra: ")
somaV = 0
somV = 0
somaE = 0
somE = 0
somaD = 0
somD = 0
while (a.upper() != "X"):
	if a.upper() == "V":
		somaV = somaV + 3
		somV = somV + 1
	elif(a.upper() == "E"):
		somaE = somaE + 2
		somE = somE + 1
	elif (a.upper() == "D"):
		somaD = somaD + 1
		somD = somD + 1
	a = input("digite uma letra: ")
	soma = somaV + somaE + somaD
	s = somV + somE + somD
a =(100*soma)/(s*3)
print(round(a,2))

