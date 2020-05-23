from numpy import*
string=array(eval(input("digite a string:")))
nivel=array(eval(input("digite o nivel:")),dtype=int)
v1=size(nivel)
i=0
soma=0
while(i<size[string]):
	if(string=="CENOURA"):
		soma=soma+(2*nivel[i])
	if(string=="FERRO"):
		soma=soma+(4*nivel[i])
	if(string=="DWARVEN"):
		soma=soma+(8*nivel[i])
	if(string=="ELVEN"):
		soma=soma+(11*nivel[i])
	if(string=="DAEDRIC"):
		soma=soma+(14*nivel[i])
dano=string*soma
print(dano)
