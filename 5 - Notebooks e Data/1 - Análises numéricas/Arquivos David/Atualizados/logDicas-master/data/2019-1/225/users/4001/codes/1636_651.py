H = float(input("Altura: "))
S = input("Gen sexual (M/F)? ")

homens = (72.7 * H) - 58
mulheres = (62.1 * H) - 44.7

if(S.upper() == "M"):
	msg = homens
else:
	msg = mulheres
print(round(msg, 2))