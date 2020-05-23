from numpy import*
mf = array(eval(input("mf: ")))
pr = array(eval(input("pr: ")))
ch = int(input("ch: "))

cont = zeros(3, dtype=int)
#cont[0]=ap #cont[1]=rn #cont[2]=rf
for i in range(size(mf)):
	if(mf[i] >= 5 and pr[i] >= (75/100)*ch):
		cont[0] = cont[0] + 1
	elif(mf[i] < 5 and pr[i] >= (75/100)*ch):	
		cont[1] = cont[1] + 1
	elif(mf[i] >= 5 and pr[i] < (75/100)*ch):
		cont[2] = cont[2] + 1
print(cont)
		