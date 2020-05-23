from numpy import*
e = array(eval(input("Jogadas de Eusapia:")))
b = array(eval(input("Jogadas de Barsanulfo:")))

print(size(e))
c = 0
ep = 0
bp = 0
p = 0


while(c!=size(e)):
	pe = e[p]
	pb = b[p]
	if((pe==11 and pb == 11) or (pe==22 and pb == 22) or (pe == 33 and pb == 33)):
		c = c+1
		p = p + 1
		
	elif((pe == 11 and pb == 33) or (pe == 22 and pb == 11) or (pe == 33 and pb == 22)):
		c = c+1
		ep = ep + 1
		p = p + 1
		
	elif((pb == 11 and pe == 33) or (pb == 22 and pe == 11) or (pb == 33 and pe == 22)):
		c = c+1
		bp = bp+1
		p = p+1
		
if(ep > bp):
	print("EUSAPIA")
elif(bp > ep):
	print("BARSANULFO")
elif(ep == bp):
	print("EMPATE")