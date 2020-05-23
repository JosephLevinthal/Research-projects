from numpy import*

v=array(eval/input(" consumo de agua"))
quant=array(eval/input("litros por semana"))
segunda=0
terca=0
quarta=0
quinta=0
sexta=0
cont=0

while(cont < size(v)):
	
	if(v[cont].upper == segunda):
	segunda=segunda+quant[cont] * 5
	if(v[cont] .upper == terca):
		terca=terca+quant[cont] * 5
	if(v[cont] .upper == quarta):
		quarta=quarta+quant[cont] * 5
	if(v[cont] . upper ==quinta):
		quinta=quinta+quant[cont] * 5
	if(v[cont] . upper == sexta):
		sexta= sexta+quant[cont] * 5
		
cont= segunda+terca+quarta+quinta+sexta
d=(quant/v)**2
print(round(d,2))