from  numpy import*
c = array(eval(input("Valor: ")))
i = 0 
d = 0
while (i < size(c)):
	if (c[i] > 80):
		c[i] = c[i] - (c[i] * 15/100) 
	else:
		c[i] = c[i]
	i = i + 1
print(round(sum(c), 2))