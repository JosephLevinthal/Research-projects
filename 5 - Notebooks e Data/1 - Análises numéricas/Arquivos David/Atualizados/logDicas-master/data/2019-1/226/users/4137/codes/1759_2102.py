from numpy import*
d = array(eval(input("Digite seu vetor")))

i = 0

while i != size(d):
	if(d[i]==0):
		d[i] = 0
	elif(d[i]%2 != 0):
		d[i] = 0
	i = i + 1
print(d)