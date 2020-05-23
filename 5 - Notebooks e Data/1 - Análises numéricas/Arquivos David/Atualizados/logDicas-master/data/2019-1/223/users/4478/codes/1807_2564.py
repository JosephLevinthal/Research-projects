from numpy import*
v1 = array(eval(input("gols da partida: ")))
v2 = array(eval(input("gols do adversario: ")))

vcont = zeros(3, dtype = int)

for i in range (0, size(v1)):
	if(v1[i]>v2[i]):
		vcont[0] = vcont[0]+1
	elif(v1[i]==v2[i]):
		vcont[1]= vcont[1]+1
	else:
		vcont[2] = vcont[2] + 1
print(vcont)