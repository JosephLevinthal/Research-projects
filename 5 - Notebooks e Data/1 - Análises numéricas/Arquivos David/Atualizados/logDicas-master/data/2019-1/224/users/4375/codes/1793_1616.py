from numpy import*
string=array(eval(input("digite o poder: ")))
v=array(eval(input("ieneso: ")),dtype=int)
v1=size(v)
i=0
soma=0
while(i<size[string]):
	if(string=="GELO"):
		soma=soma+(2*v[i])
	if(string=="FOGO"):
		soma=soma+(3*v[i])
	if(string=="CHOQUE"):
		soma=soma+(4*v[i])
	if(string=="CONJURACAO"):
		soma=soma+(8*v[i])
	if(string=="ILUSAO"):
		soma=soma+(10*v[i])
dano=string*soma
print(dano)