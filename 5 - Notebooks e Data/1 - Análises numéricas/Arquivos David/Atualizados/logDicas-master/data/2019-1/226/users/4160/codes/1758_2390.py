from numpy import*
vp = array(eval(input("Presentes por mes: ")))
vf = array(eval(input("Faltosos por mes: ")))

i=0
a = max(vp)
mes = 1
while(vp[i]!=max(vp)):
	mes = mes + 1 
	i = i + 1
print (mes)