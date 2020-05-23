from numpy import*
t_chegada=array(eval(input("tempo: ")))
crescente=arange(size(t_chegada))
cont=0
con=0
while(t_chegada[cont]!=min(t_chegada)):
	cont=cont+1
print(crescente[cont])
