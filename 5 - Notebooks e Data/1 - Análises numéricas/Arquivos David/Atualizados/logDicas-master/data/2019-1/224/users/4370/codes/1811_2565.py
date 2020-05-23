from numpy import *
medias = array(eval(input("digite o vetor medias: ")))
pres = array(eval(input("digite as presencas: ")))
h = int(input("digite a carga horaria: "))
ap = 0
repn = 0
repf = 0
for i,j in zip(medias, pres):
	if(i >= 5 and j >= h*(75/100)):
		ap = ap + 1
	if(i < 5):
		repn = repn + 1
	if(j < h*(75/100)):
		repf = repf + 1
z = zeros(3,dtype = int)
z[0] = ap
z[1] = repn
z[2] = repf
print(z)
