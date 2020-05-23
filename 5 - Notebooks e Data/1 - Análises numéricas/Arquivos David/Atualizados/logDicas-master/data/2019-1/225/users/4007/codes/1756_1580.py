from numpy import*
p = array(eval(input("nota dos alunos: ")))
n = array(eval(input("nome: ")))

f = 0
ap = 0
rep = 0
mep = 0
cont = 0
while (cont < size(p)):
	if (p[cont] == -1):
		f = f + 1
		
	elif (p[cont] >= 6):
		ap = ap + 1
		
	elif (p[cont] < 6 and p[cont] > -1):
		rep = rep + 1
	
	cont = cont + 1    
	
print(f)
print(ap)
print(rep)

t = []
c = 0
while(c < size(p)):
	if(p[c] >= 0):
		t.append(p[c])
	c = c + 1
media = sum(t)/size(t)
print(round(media, 2))
i = 0
while (p[i] != max(p)):
	i = i + 1
print(n[i])
	

	
	
	
	
	
	
	 
	
	