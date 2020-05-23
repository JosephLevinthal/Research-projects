from numpy import *
notas = array(eval(input("Notas: ")))
nomes = array(eval(input("Nomes: ")))

f = 0
ap = 0
rp = 0
nt = 0
i = 0
j = 0

while(i < size(notas)):
	if(notas[i] == -1):
		f = f + 1
		
	if(notas[i] >= 6):
		ap = ap + 1
		
	if(notas[i] < 6 and notas[i] >= 0):
		rp = rp + 1

	if(notas[i] >= 0):
		nt = nt + notas[i]
	i = i + 1

	if(notas[j] != max(notas)):
		j = j + 1
	
print(f)
print(ap)
print(rp)
print(round(nt/(ap+rp),2))
print(nomes[j])