from numpy import*
ma = array(eval(input("Media do Aluno: ")))
p = array(eval(input("Precenca em Horas: ")))
ch = int(input("Carga Horaria: "))
lol = zeros(3,dtype=int)

for i in range(size(ma)): 
	dd = (75 / 100) * ch
	
	if ma[i] >= 5 and p[i] >= dd: 
		lol[0]= lol[0] + 1
	elif ma[i] < 5: 
		lol[1]= lol[1] + 1
	else: 
		lol[2] = lol[2] + 1
print(lol)	