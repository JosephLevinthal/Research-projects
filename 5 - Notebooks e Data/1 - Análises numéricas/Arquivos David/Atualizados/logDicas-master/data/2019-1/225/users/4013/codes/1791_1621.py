from numpy import*
v = array(input("nomes dos produtos:"))
quant = array(eval(input("quantidades de cada:")))
i = 0
j = 0
custo = 0 
a=0
b=0
c=0
d=0
e=0
while(i < size(v)): 
	quant[j] = quant[j] * v[i]
	if(v[i] == "ARROZ"):
		custo = custo + 1.25
		a=a+custo
	elif(v[i] == "FEIJAO"):
		custo = custo + 2.60
		b= b+custo
	elif(v[i] == "BIS"):
		custo = custo + 1.80
		c= c+custo
	elif(v[i] == "MIOJO"):
		custo = custo + 0.85
		d = d+custo
	elif(v[i] == "FANTA"):
		custo = custo + 3.20
		e=e+custo
	i =i + 1
	j = j + 1
	total = a+b+c+d+e
print(round(total ,2))
	