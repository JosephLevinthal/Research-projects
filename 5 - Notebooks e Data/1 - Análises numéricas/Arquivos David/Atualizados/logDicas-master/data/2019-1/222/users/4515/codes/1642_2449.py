cfa = float(input("Coeficiente A :"))
cfb = float(input("Coeficiente B :"))
cfc = float(input("Coeficiente C :"))
cfd = float(input("Coeficiente D :"))
cfe = float(input("Coeficiente E :"))
cff = float(input("Coeficiente F :"))

divisor = (cfa*cfe)-(cfb*cfd)

if(divisor != 0):
	x = ((cfc * cfe)-(cfb*cff)) / divisor 
	y = ((cfa * cff)-(cfc*cfd)) / divisor
	print(x) 
	print(y)
else:	
	print("Nao tem solucao")
	