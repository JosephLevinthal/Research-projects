dt= int(input("insira a data (ddmmaaaa): "))
d=dt//1000000
ms=(dt//10000)%100
an=dt%10000
if an>0 and ms>=1 and ms<=12 and d>=1 and d<=31:
	if((an%400 == 0) or((an%100 != 0) and(an%4 == 0)) and ms==2 and d<=29):
		print(d,"de",ms,"de",an,"eh uma data valida")
	elif((an%400 == 0) or((an%100 != 0) and(an%4 == 0))and ms==2 and d>29):
		print(d,"de",ms,"de",an,"nao eh uma data valida")
	elif not((an%400 == 0) or((an%100 != 0) and(an%4 == 0)))and ms==2 and d>28:
		print(d,"de",ms,"de",an,"nao eh uma data valida")
	elif not((an%400 == 0) or((an%100 != 0) and(an%4 == 0)))and ms==2 and d<=28:
		print(d,"de",ms,"de",an,"eh uma data valida")
	elif an==1582 and ms==10 and d>=5 and d<=14:
		print(d,"de",ms,"de",an,"nao eh uma data valida")
	elif (ms==1 or ms==3 or ms==5 or ms==7 or ms==8 or ms==10 or ms==12) and d<=31:
		print(d,"de",ms,"de",an,"eh uma data valida")
	elif (ms==4 or ms==6 or ms==9 or ms==11) and d<=30:
		print(d,"de",ms,"de",an,"eh uma data valida")
	elif (ms==4 or ms==6 or ms==9 or ms==11) and d>30:
		print(d,"de",ms,"de",an,"nao eh uma data valida")
else:
	print(d,"de",ms,"de",an,"nao eh uma data valida")