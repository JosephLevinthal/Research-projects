a=float(input(":"))

if(a<=10000):
	custo=(5.00*a)
	print(round(custo,2))
if(a>=10000):
	conta=(5.00*a)+a-1000
print(round(conta,2))