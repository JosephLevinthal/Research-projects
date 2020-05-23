from numpy import*
r = array(eval(input("insira o numero de termos; ")))

i = 0
p = 0
n = 0

while(i<size(r)):
	if r[i]>0:
		p = p + 1
	else:
		n = n + 1
	i = 1 + i
	
lista_valida = zeros(p, dtype=int)
e = 0
a = 0
while (a < size(lista_valida)):
	if(r[e]>0):
		lista_valida[a] = r[e] 
		a = a + 1
		e = e +1
	else:
		e = e +1
print(lista_valida)