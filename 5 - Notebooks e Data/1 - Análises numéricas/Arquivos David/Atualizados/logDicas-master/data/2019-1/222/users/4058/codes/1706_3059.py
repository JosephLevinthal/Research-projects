a=float(input("qual o consumo?"))
if a>0 and a<=100:
	valor= (a* 1.20)+1
	print(round(valor,2))
elif a>100 and a<=200:
	valor= (a* 1.30)+10
	print(round(valor,2))
elif a>200 and a<=300:
	valor= (a* 1.40)+20
	print(round(valor,2))
else:
	valor= (a* 1.50)+25
	print(round(valor,2))

