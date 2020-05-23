from numpy import*

x = array(eval(input("Digite os valores: ")))
d1 = 0
media = sum(x)/size(x)

for i in range(size(x)):
	d = (x[i] - media) ** 2	
	d1 = d1 + d 
desvio = sqrt(d1 / (size(x) - 1))
 
print(round(desvio, 3))