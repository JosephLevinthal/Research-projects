a = input("Senha: ")
i = 0 
b = len(a)
for x in a:
	while(b>=i)and(b>=8):
		if(a[x].islower()) and (a[x].isupper()):
			print("SENHA VALIDA")
		i+=1
		
	else:
		print("SENHA INVALIDA ")