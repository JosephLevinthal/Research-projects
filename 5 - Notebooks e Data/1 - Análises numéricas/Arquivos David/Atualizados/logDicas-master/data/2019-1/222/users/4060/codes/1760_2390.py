from numpy import*
presentes=array(eval(input("presentes: ")))
faltantes=array(eval(input("faltantes: ")))
pre_menos_fal=presentes-faltantes
cont=0
i=0
crescente=arange(size(presentes))

while(cont!=max(pre_menos_fal)):
	i=i+1
	cont=cont+1
print(pre_menos_fal)