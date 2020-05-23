x = float(input())

if(x <= 1659.38):
	x = x - ((x * 8) / 100)
elif(x >= 1659.39 and x <= 2765.66):
	x = x - ((x * 9) / 100)
elif(x >= 2765.67 and x <= 5531.31):
	x = x - ((x * 11) / 100)
elif(x > 5531.31):
	x = x - 608.44
	
if(x <= 1903.98):
	x = x - 0
elif(x >= 1903.99 and x <= 2826.65):
	x = x - ((x * 7.5) / 100)
elif(x >= 2826.66 and x <= 3751.05):
	x = x - ((x * 15) / 100)
elif(x >= 3751.06 and x <= 4664.68):
	x = x - ((x * 22.5) / 100)
elif(x > 4664.68):
	x = x - ((x * 27.5) / 100)
	
print("Salario liquido = R$ ", round(x, 2))