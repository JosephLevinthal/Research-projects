nha = int(input("Numero de habitantes de A: "))
nhb = int(input("Numero de habitantes de B: "))
pca = float(input("Percentual de crescimnto de A: "))
pcb = float(input("Percentual de crescimnto de B: "))

acumulador = 0


while (nhb  > nha ):
	nha = nha*((pca + 100)/100)	
	nhb = nhb*((pcb + 100)/100)
	acumulador = acumulador + 1
print(acumulador)