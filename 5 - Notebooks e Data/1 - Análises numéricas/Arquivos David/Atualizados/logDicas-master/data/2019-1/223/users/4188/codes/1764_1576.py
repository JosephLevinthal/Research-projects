from numpy import *
e = array(eval(input("eusapia: ")))
b = array(eval(input("barsanulfo: ")))
p = 0
ce = 0
cb = 0
while (p < size(e)):
	if (e[p]==11):
		if (b[p]==22):
			cb = cb + 1
		elif (b[p]==33):
			ce = ce + 1
	elif (e[p]==22):
		if (b[p]==11):
		 	ce = ce + 1
		elif(b[p]==33):
		 	cb = cb + 1
	elif (e[p]==33):
		if(b[p]==11):
		 	cb = cb + 1
		elif(b[p]==22):
		 	ce = ce + 1
	p=p+1
print(size(e))
if (sum(ce) > sum(cb)):
	print("EUSAPIA")
elif (sum(ce) < sum(cb)):
	print("BARSANULFO")
else:
	print("EMPATE")
		 