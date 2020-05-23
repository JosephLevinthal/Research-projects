a=int(input("habitantes_da_cidade_a: "))
b=int(input("habitantes_da_cidade_b: "))
pa=float(input("percentual_da_cidade_a: "))
pb=float(input("percentual_da_cidade_b: "))
soma=0
while(a<b):
	a=((a*pa)/100)+a
	b=((b*pb)/100)+b
	soma=soma+1
print(soma)
	
	