from numpy import *

e = array(eval(input("insira:")))
b = array(eval(input("insira:")))

i = 0
eusa = 0
bars = 0
while i < size(b):
	if(e[i] == 11 and b[i] == 33):
		eusa = eusa + 1
	elif(e[i] == 22 and b[i] == 11):
		eusa = eusa + 1
	elif(e[i] == 33 and b[i] == 22):
		eusa = eusa + 1
	elif(b[i] == 11 and e[i] == 33): 
		bars = bars + 1
	elif(b[i] == 22 and e[i] == 11): 
		bars = bars + 1
	elif(b[i] == 33 and e[i] == 22):
		bars = bars + 1
	i = i + 1
print(i)
if(eusa > bars):
	print("EUSAPIA")
elif(eusa < bars):
	print("BARSANULFO")
else:
	print("EMPATE")
	
