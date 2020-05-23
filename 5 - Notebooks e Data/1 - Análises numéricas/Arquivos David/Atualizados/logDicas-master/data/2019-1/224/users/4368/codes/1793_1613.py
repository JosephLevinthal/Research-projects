from numpy import*
x=array(eval(input("digite o nome das atividades fisicas: ")))

y=array(eval(input("digite o tempo das atividades: ")))
t=0
h=0
while(size(x)>h):
	x[h]=str(x[h]).upper()
	if(x[h])=="ALONGAMENTO":
		t=t+(y[h]*3)
		h=h+1
		
	elif(x[h])=="CORRIDA":
		t=t+(y[h]*10.3)
		h=h+1

	elif(x[h])=="DANÇA":
		t=t+(y[h]*6.7)
		h=h+1
	
	elif(x[h])=="ESCALADA":
		t=t+(y[h]*9.7)
		h=h+1
		
	elif(x[h])=="HIDROGINASTICA":
		t=t+(y[h]*5)
		h=h+1

		
print(round(t,2))
