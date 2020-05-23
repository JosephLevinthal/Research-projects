p=int(input("primeiro valor: "))

CO=1
SINAL=1
D1=2
D2=3
D3=4
SOMA=3
while(p>CO):
	SOMA=SOMA+((SINAL)*(4/(D1*D2*D3)))
	SINAL*=-1
	D1+=2
	D2+=2
	D3+=2
	CO+=1
print(round(SOMA,8))