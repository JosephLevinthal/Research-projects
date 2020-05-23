q= int(input("insira o dia do mes entre(1-31): "))
ms= int(input("insira o mes entre(1-12): "))
a= int(input("insira o ano: "))
k=a%100
j=a/100
k1=(a-1)%100
j1=(a-1)/100
h= (q+((13*(ms+1))//5)+k+(k//4)+(j//4)+5*j)%7
hjf=(q+((13*((ms+12)+1))//5)+k1+(k1//4)+(j1//4)+5*j1)%7
h1=int(h)
h2=int(hjf)
if not(ms==1 or ms==2):
	if (h1==0):
		print("sabado")
	elif (h1==1):
		print("domingo")
	elif (h1==2):
		print("segunda-feira")
	elif (h1==3):
		print("terca-feira")
	elif (h1==4):
		print("quarta-feira")
	elif (h1==5):
		print("quinta-feira")
	elif (h1==6):
		print("sexta-feira")
elif (ms==1)or(ms==2):
	if (h2==0):
		print("sabado")
	elif (h2==1):
		print("domingo")
	elif (h2==2):
		print("segunda-feira")
	elif (h2==3):
		print("terca-feira")
	elif (h2==4):
		print("quarta-feira")
	elif (h2==5):
		print("quinta-feira")
	elif (h2==6):
		print("sexta-feira")