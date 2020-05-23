x=int(input("Digite o ano: "))
a=x%1000000
mes=a//10000
ano=x%10000
data=x//1000000
u="eh uma data valida"
z="nao eh uma data valida"
t=0
g=0
if(ano<=0)or((mes<1)and(mes>12)):
	t=z
elif(ano%400==0):
	g=1
elif(ano%4==0)and(ano%100!=0):
	g=1
elif(ano==1582):
	g=2
else:
	g=3
if(g==2):
	if(mes==1):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==2):
		if(data>=1)and(data<=28):
			t=u
		else:
			t=z
	if(mes==3):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==4):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==5):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==6):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==7):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==8):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==9):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==10):
		if(data>=1)and(data<=31)and(data<5)and(data>14):
			t=u
		else:
			t=z
	if(mes==11):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==12):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
if(g==1):
	if(mes==1):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==2):
		if(data>=1)and(data<=29):
			t=u
		else:
			t=z
	if(mes==3):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==4):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==5):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==6):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==7):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==8):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==9):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==10):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==11):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==12):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z				
if(g==3):
	if(mes==1):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==2):
		if(data>=1)and(data<=28):
			t=u
		else:
			t=z
	if(mes==3):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==4):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==5):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==6):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==7):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==8):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==9):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==10):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z
	if(mes==11):
		if(data>=1)and(data<=30):
			t=u
		else:
			t=z
	if(mes==12):
		if(data>=1)and(data<=31):
			t=u
		else:
			t=z	
print(data,"de",mes,"de",ano,t)			
					
					
					
					
					
					
					
					
					
					
					
			


	
	
	

	
			
	