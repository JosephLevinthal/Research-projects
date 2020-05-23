from numpy import*
etr= array(eval(input("vetor de pessoas que entraram: ")))
srm= array(eval(input("pessoas que sairam: ")))
rest=0
parada=0
while (parada<size(etr)):
	rest= rest + (etr[parada] - srm[parada])
	parada= parada + 1
if (rest>=75):
	rest=75
	print(rest)
else:
	print(rest)

	