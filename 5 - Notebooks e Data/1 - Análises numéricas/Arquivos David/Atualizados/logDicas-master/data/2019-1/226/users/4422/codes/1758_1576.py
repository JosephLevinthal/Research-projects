from numpy import*
eu = array(eval(input("eu: ")))
ba = array(eval(input("bar: ")))

i = 0
ve = 0
vb = 0

while(i<size(ba) and size(eu)==size(ba)):
	if((eu[i] == 11 and ba[i] == 33) or (eu[i] == 22 and ba[i] == 11) or (eu[i] == 33 and ba[i] == 22)):
		i = i + 1
		ve = ve + 1
	elif((ba[i] == 11 and eu[i] == 33) or (ba[i] == 22 and eu[i] == 11) or (ba[i] == 33 and eu[i] == 22)):
		i = i + 1
		vb = vb + 1
	else:
		i = i + 1
print(i)
if(ve>vb):
		print("EUSAPIA")
elif(vb>ve):
		print("BARSANULFO")
else:
		print("EMPATE")