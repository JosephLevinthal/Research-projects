t = input("")
v = int(input("digite o valor do dado: "))
n = int(input("numero de turnos: "))
if(t!="CAUDA") and (t!="CUSPE") and (t!="PATADA") and (v<1) and (v>4):
	print("Entrada invalida")
elif(t =="CAUDA")and (v== 1):
	print(v*n)
elif(t=="CAUDA")and(v==2):
	print(v*n)
elif(t=="CAUDA")and(v==3):
	print(v*n)
elif(t=="CAUDA")and (v==4):
	print(v*n)
elif(t=="CUSPE") and (v==1):
	print(2*v*n)
elif(t=="CUSPE") and (v==2):
	print(2*v*n)
elif(t=="CUSPE") and (v== 3):
	print(2*v*n)
elif(t=="CUSPE")and (v==4):
	print(2*v*n)