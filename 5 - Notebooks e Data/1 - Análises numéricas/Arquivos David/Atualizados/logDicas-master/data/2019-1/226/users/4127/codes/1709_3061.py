atq= input("qual o tipo de ataque?").upper()
unid= int(input("qual a quantidade de unidades a serem destruidas? "))

if (unid<0 or atq!="TERRESTRE" and atq!="AEREO" and atq!="MARITIMO"):
	print("Entrada invalida")
elif (atq=="TERRESTRE"):
	x= (unid//150)+1
	print("DROGON")
	print(x)
elif (atq=="AEREO"):
	x=(unid//30)+1
	print("RHAEGAL")
	print(x)
elif (atq=="MARITIMO"):
	x=(unid//40)+1
	print("VISERION")
	print(x)