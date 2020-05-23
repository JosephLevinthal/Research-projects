from numpy import*

p = array(eval(input("presentes:")))
f = array(eval(input("faltantes:")))
i = 0 #CONTADORA	
fa = 0 #FALTANTES
pg = 0 #	PRESENTES GERAL
while(i != size(p)):
	pg = p - f
	if(pg[i] == max(pg)):
		m = i
	i = i + 1
print(m+1)