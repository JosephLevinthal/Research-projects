percurso=float(input("p"))
tipo=input("t")
consumoa=percurso/8
consumob=percurso/12
if(tipo.upper() == "A" ):
	print(round(consumoa,2))
else:
	print(round(consumob,2))
