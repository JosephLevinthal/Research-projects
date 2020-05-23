from numpy import * 
notas= array(eval(input("aprovados:")))

while(size(notas) > 1):
	soma = 0
	for i in notas:
		if(i >= 5 and i < 7):
			soma = soma + 1
		
	print(soma)
	
	notas= array(eval(input("aprovados:")))