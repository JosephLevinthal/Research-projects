from numpy import * 
glic = array(eval(input("Glicose: ")))

i= 0
cont = 0 # Ocorrencia

while(i < size(glic)):
	if(glic[i]> 99):
		print(i)
		cont = cont+1
	i = i + 1
print(cont)