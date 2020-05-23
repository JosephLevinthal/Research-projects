pre = float(input("X:"))
pag = float(input("y:"))
if(pre>pag):
	dif=pre-pag
	print("Falta",round(dif,2))
else:
	dif=pag-pre
	print("Troco de",round(dif,2))