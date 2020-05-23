num=int(input("digite um numero: "))
contadora=1
apr=1/12
pt=0
denominador=0
while(contadora<num):
	if(denominador>1):
		denominador=contadora*3**pt
	else:
		denominador=contadora*(3**(pt+1))
		apr=apr+(-1)**(contadora)*1/denominador
	
	contadora=contadora+1
	
print(round(apr, 8))