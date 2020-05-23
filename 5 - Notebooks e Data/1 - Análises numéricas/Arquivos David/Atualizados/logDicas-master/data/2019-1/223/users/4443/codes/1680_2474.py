# Teste seu código com o dia do seu nascimento. Deu certo? E o dia de hoje?

# Que importante cientista nasceu em 4 de janeiro de 1643?

q = int(input("Digite o dia do mes: "))
m = int(input("Digite o mes: "))
k = int(input("Digite o ano: "))
j = int(k/100)
k = k%100

if (1<= m <=2):
	m = m + 12
	k = k-1
	h = (q+int((13*(m+1)/5))+k+int(k/4)+int(j/4)+5*j)%7
	if(h == 0):
		print("sabado")
	elif(h == 1):	
		print("domingo")
	elif(h == 2):	
		print("segunda-feira")
	elif(h == 3):	
		print("terca-feira")		
	elif(h == 4):	
		print("quarta-feira")		
	elif(h == 5):	
		print("quinta-feira")		
	elif(h == 6):	
		print("sexta-feira")		
else:
	h = (q+int((13*(m+1))/5)+k+int(k/4)+int(j/4)+5*j)%7
	if(h == 0):
		print("sabado")
	elif(h == 1):	
		print("domingo")
	elif(h == 2):	
		print("segunda-feira")
	elif(h == 3):	
		print("terca-feira")		
	elif(h == 4):	
		print("quarta-feira")		
	elif(h == 5):	
		print("quinta-feira")		
	elif(h == 6):	
		print("sexta-feira")		