from math import*

raio= float(input("Didite o valor do raio :"))
h= float(input("digite o valor da altura :"))
n=int(input("1/2:"))
v1=( pi * (h  ** 2)) * ( 3 * raio - h)/ 3
v2=(4 * pi)*(raio ** 3)/ 3

df= v2-v1

if(n==1): 
	print(round(v1, 4))
else:
	print(round(df, 4))
