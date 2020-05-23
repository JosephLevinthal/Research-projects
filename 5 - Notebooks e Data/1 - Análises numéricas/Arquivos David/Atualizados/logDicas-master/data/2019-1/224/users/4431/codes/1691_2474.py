q=int(input("Digite o dia do mes "))
m=int(input("Digite o mes: "))
g=int(input("Digite o ano: "))
if(m==1)or(m==2):
	m=m+12
	g=g-1

k=g%100
j=int(g/100)
h=(q+((13*(m+1))/5)+k+(k/4)+(j/4)+5*j)%7
h=int(h)
if(h==1):
	   h="domingo"
elif(h==2):
	   h="segunda-feira"
elif(h==3):
	   h="terca-feira"
elif(h==4):
	   h="quarta-feira"
elif(h==5):
      h="quinta-feira"
elif(h==6):
	   h="sexta-feira"
elif(h==0):
	   h="sabado"
print(h)	