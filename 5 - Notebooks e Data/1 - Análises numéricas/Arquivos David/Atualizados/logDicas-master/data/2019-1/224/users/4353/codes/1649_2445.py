a=input("em que temperatura esta representada: ")
b=float(input("valor da temperatura: "))
fi=5/9*(b-32)
ci=b*1.8+32
if(a.upper()=="F"):
	print(round(fi,2))
else:
	if(a.upper()=="C"):
		print(round(ci,2))