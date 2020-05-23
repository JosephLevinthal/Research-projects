qi = int(input("Quantidade inicial: "))
p = int(input("Percentual de crescimento: "))
qa = int(input("Quantidade anual: "))
percentual = p/ 100
limite = 12000
t = 0
while(qi > 0 and qi < limite):
	qi = qi - qa + (qi*percentual)
	t = t + 1
	if(qi>=limite):
		x = "LIMITE"
	else:
		x = "EXTINCAO"
print(x)		
print(t)