from math import*
k=int(input("vlaor de k: "))

CO=1
soma=1
divi=1

while(CO<k):
	soma=soma+((1)/factorial(divi))
	divi=divi+1
	CO+=1
print(round(soma,8))