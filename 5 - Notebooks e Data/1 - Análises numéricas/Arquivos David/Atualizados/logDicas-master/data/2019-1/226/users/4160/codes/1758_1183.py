from numpy import*
v = array(eval(input("Vetor: ")))

# Cortar os negativos:
i = 0 #qnt positivos
f = 0 #copiar os positivos pra saida

while(i<size(v)):
	if(v[i]>0):
		f = f + 1
	i = i + 1

v1 = zeros(f,dtype=int)
t=0
g=0

while(t<size(v)):
	if(v[t]>0):
		v1[g] =v[t]
		g = g +1
	t = t + 1
		
print(v1)
