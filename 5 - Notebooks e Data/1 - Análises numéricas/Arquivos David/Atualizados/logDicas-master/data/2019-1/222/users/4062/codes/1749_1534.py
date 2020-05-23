from math import*
cont=0
soma=0
exp=1
x= float(input("num1: "))
k= int(input("num2: "))
while((x>-1) and (x<1) and (k>0)):
	soma= soma + cont
	cont= cont + 1
	exp= exp + 2
	a=(x ** exp) / (exp)
print(round(a, 7)