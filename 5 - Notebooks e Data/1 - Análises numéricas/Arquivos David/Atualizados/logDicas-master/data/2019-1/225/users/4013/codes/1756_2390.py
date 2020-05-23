from numpy import*
vec1 = array(eval(input("digite:"))) #quant de presentes por mes
vec2 = array(eval(input("digite:"))) #quant de faltantes por mes

i = 0
while(i <= 11):
	if(vec1[i] == max(vec1)):
		print(i + 1)
	i = i + 1