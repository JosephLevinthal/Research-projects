from numpy import*
v = array(eval(input("")))
qtd = 0
for i in range(len(v)):
	if v[i]%5 == 0 :
		qtd = qtd + 1
v2 = zeros(qtd, dtype = int)
c = 0
for i in range(len(v)):
	if v[i]%5 == 0:
		v2[c] = 1
		c = c + 1
print(qtd)
print(v2)	