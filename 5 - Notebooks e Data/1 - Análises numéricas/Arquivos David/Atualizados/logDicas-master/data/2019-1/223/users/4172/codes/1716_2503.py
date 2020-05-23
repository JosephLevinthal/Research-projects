n=int(input("numero natural: "))

co=1
sinal=-1
soma=4/1
den=3

while(n>co):
	soma=soma+(sinal*(4/den))
	sinal*=-1
	den+=2
	co+=1
print(round(soma,8))