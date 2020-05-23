percurso=float(input());
tipo=input().upper();

if(tipo=="A"):
	gasto=percurso/8;
	print(round(gasto,2));
if(tipo=="B"):
	gasto=percurso/12;
	print(round(gasto,2))