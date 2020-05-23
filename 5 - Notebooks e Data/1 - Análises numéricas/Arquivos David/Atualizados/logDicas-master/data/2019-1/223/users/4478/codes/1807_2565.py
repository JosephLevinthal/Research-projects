from numpy import*
v1 = array(eval(input("medias finais: ")))
v2 = array(eval(input("presenca")))
ch = int(input("carga horaria: "))
freq = 75/100 * ch
vcont = zeros(3, dtype = int)
for i in range (size(v1)):
	if(v1[i]>=5 and v2[i] >= freq):
		vcont[0] = vcont[0] + 1
	elif(v1[i]< 5 and v2[i]>=freq):
		vcont[1] = vcont[1] + 1
	else:
		vcont[2] = vcont[2] + 1
print(vcont)
