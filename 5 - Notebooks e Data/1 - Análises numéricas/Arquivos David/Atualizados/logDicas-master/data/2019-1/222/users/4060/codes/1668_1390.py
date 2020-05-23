c=float(input("consumo de minutos: "))
tar=c*1.20
jur=(c*1.40)+25
if(c<=100):
	print(round(tar,2))
else:
	print(round(jur,2))
 