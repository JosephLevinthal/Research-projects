h=float(input())
sexo=input().upper();

if(sexo=="M"):
	x=(72.7*h)-58;
	print(round(x,2));
if(sexo=="F"):
	y=(62.1*h)-44.7;
	print(round(y,2));
