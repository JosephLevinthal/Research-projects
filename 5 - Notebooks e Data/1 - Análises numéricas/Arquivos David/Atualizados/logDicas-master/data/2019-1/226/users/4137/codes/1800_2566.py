from numpy import*

f = array(eval(input("Faltas:")))

d = zeros(6, dtype = float)

for i in range(size(f)):
	if(f[i]==2):
		d[0] = d[0] + 1
	elif(f[i]==3):
		d[1] = d[1] + 1
	elif(f[i]==4):
		d[2] = d[2] + 1
	elif(f[i]==5):
		d[3] = d[3]+1
	elif(f[i]==6):
		d[4] = d[4]+1
	elif(f[i]==7):
		d[5] = d[5]+1

d[0] = round((d[0]*100) / size(f), 1)
d[1] = round((d[1]*100) / size(f), 1)
d[2] = round((d[2]*100) / size(f), 1)
d[3] = round((d[3]*100) / size(f), 1)
d[4] = round((d[4]*100) / size(f), 1)
d[5] = round((d[5]*100) / size(f), 1)

print(d)