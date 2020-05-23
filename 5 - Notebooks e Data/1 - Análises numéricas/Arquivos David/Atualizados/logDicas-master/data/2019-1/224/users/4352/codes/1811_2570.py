from numpy import*
x = array(eval(input("digite um vetor de numeros reais: ")))
a = 1
m = sum(x)/size(x)
for i in x:
	a = a * abs(i - m)
	p = (a)**(1/size(x))
print(round(p, 3))