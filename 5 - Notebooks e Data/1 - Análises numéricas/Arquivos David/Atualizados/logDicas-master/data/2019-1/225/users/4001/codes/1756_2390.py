from numpy import*
p = array(eval(input("Presentes: "))) 
f = array(eval(input("Faltantes: ")))
i = 0
r = 1
while (p[i] != max(p)):	
	i = i + 1
	r = r + 1
print(r)