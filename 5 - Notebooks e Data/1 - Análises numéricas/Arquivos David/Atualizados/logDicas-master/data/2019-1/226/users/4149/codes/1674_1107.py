h=int(input("entre com o dia de hoje "))
f=int(input("entre com o numero de dias futuro "))
fu=(h+f)%7
if(h>=0)and(h<=6):
	if(f>0):
		if(h==0):
			x="domingo"
		elif(h==1):
			x="segunda"
		elif(h==2):
			x="terca"
		elif(h==3):
			x="quarta"
		elif(h==4):
			x="quinta"
		elif(h==5):
			x="sexta"
		elif(h==6):
			x="sabado"
		if(fu==0):
					y="domingo"
		elif(fu==1):
					y="segunda"
		elif(fu==2):
					y="terca"
		elif(fu==3):
					y="quarta"
		elif(fu==4):
					y="quinta"
		elif(fu==5):
					y="sexta"
		elif(fu==6):
					y="sabado"
		print("Hoje eh",x,"e o dia futuro eh",y)
	else:
		print("A entrada",f,"eh invalida")	

else:
	print("A entrada",h,"eh invalida")

		
