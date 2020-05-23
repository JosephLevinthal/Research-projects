from numpy import*
e = (array(eval(input("Vet 1:"))))
b = (array(eval(input("Vet 2:"))))

print(size(e))

i = 0
ve = 0
vb = 0

while(i<size(e) and size(e)==size(b)):
	pe = e[i]
	pb = b[i]
	if((pe==11 and pb==33)or(pe==22 and pb==11)or(pe==33 and pb==22)):
		i = i+1
		ve = ve+1
	elif((pb==11 and pe==33)or(pb==22 and pe==11)or(pb==33 and pe==22)):
		i = i+1
		vb = vb+1
	else:
		i = i+1

if(ve>vb):
	print("EUSAPIA")
elif(vb>ve):
	print("BARSANULFO")
else:
	print("EMPATE")
		
		