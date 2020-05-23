from numpy import*
pali=input("write phrase: ")
cop=""
i=0
while(i<len(pali)):
	if(pali[i]==" "):
		cop = cop + ""
	else:
		cop = cop + str(pali[i])
	i=i+1
print(cop.upper())
valor=0
i2=0
while(i2<len(cop)):
	if(cop[i2]==cop[-1*(i2+1)]):
		valor=valor+1
	else:
		valor=valor+0
	i2=i2+1
if(valor==len(cop)):
	print("1")
else:
	print("0")

	