from numpy import*
v = array(eval(input("digite os numeros: ")))
i = 0
m = 0
while(i<size(v)):
	m = m + (v[i]**(1/6))
	i = i+1
print(round((m/size(v))**6,2))