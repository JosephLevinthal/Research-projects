from numpy import*

v = array(eval(input("vetor de custo dos itens: ")))

i = 0         #contador/indice
d = 15/100    #desconto
s = size(v)   #tamanho
r = zeros(s, dtype = float) #vetor reflexo

while i < s:
	if v[i] <= 80:
		r[i] = v[i]
		i = i + 1
	else:
		r[i] = v[i] * (1 - d)
		i = i + 1
t = sum(r)
print(round(t, 2))
	