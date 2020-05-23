from numpy import *

eusa = array(eval(input()))
barsa = array(eval(input()))

VitE = 0
VitB = 0
cont = 0

while (cont < len(eusa)):
	while (eusa[cont] == 11 and barsa[cont] == 22):
		VitB+=1
		eusa[cont] = eusa[cont] + 1
	while (eusa[cont] == 11 and barsa[cont] == 33):
		VitE+=1
		eusa[cont] = eusa[cont] + 1
	while (eusa[cont] == 22 and barsa[cont] == 11):
		VitE+=1
		eusa[cont] = eusa[cont] + 1
	while (eusa[cont] == 22 and barsa[cont] == 33):
		VitB+=1
		eusa[cont] = eusa[cont] + 1
	while (eusa[cont] == 33 and barsa[cont] == 11):
		VitB+=1
		eusa[cont] = eusa[cont] + 1
	while (eusa[cont] == 33 and barsa[cont] == 22):
		VitE+=1
		eusa[cont] = eusa[cont] + 1
	cont+=1

print(cont)
if (VitE > VitB):
	print("EUSAPIA")
elif(VitE < VitB):
	print("BARSANULFO")
else:
	print("EMPATE")
	
'''from numpy import *

eusa = array(eval(input()))
barsa = array(eval(input()))

VitE = 0
VitB = 0
cont = 0

while (cont < len(eusa)):
	if (eusa[cont] == 11 and barsa[cont] == 22):
		VitB+=1
	elif (eusa[cont] == 11 and barsa[cont] == 33):
		VitE+=1
	elif (eusa[cont] == 22 and barsa[cont] == 11):
		VitE+=1
	elif (eusa[cont] == 22 and barsa[cont] == 33):
		VitB+=1
	elif (eusa[cont] == 33 and barsa[cont] == 11):
		VitB+=1
	elif (eusa[cont] == 33 and barsa[cont] == 22):
		VitE+=1
	cont+=1

print(cont)
if (VitE > VitB):
	print("EUSAPIA")
elif(VitE < VitB):
	print("BARSANULFO")
else:
	print("EMPATE")'''