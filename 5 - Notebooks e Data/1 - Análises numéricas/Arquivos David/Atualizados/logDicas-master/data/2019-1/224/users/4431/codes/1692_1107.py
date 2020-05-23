x=int(input("Entre com o numero do dia de hoje: "))
if(x!=0)and(x!=1)and(x!=2)and(x!=3)and(x!=4)and(x!=5)and(x!=6):
	print("A entrada",x,"eh invalida")
elif(x==0):
	y="domingo"
elif(x==1):
	y="segunda"
elif(x==2):
	y="terca"
elif(x==3):
	y="quarta"
elif(x==4):
   y="quinta"
elif(x==5):
	y="sexta"
elif(x==6):
	y="sabado"
	
if(x!=0)and(x!=1)and(x!=2)and(x!=3)and(x!=4)and(x!=5)and(x!=6):
	p=0
else:	
   a=int(input("Entre com o numero de dias apos hoje: "))
   h=(a+x)%7
   if(h==0):
	   h="domingo"
   elif(h==1):
	   h="segunda"
   elif(h==2):
	   h="terca"
   elif(h==3):
	   h="quarta"
   elif(h==4):
      h="quinta"
   elif(h==5):
	   h="sexta"
   elif(h==6):
	   h="sabado"
		
	
if(x!=0)and(x!=1)and(x!=2)and(x!=3)and(x!=4)and(x!=5)and(x!=6):	
	v=0
else:
	print("Hoje eh",y,"e o dia futuro eh",h)
	
	


	

	


	
   

