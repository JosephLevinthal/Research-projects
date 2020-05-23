from numpy import*
v = array(eval(input("faltas: ")))

seg = 0
ter = 0
qua = 0 
qui = 0
sex = 0
sab = 0

for i in range (size(v)):
	if(v[i] == 2):
	 	seg = seg + 1
	elif(v[i] == 3):
		ter = ter + 1
	elif(v[i] == 4):
		 qua = qua + 1
	elif(v[i] == 5):
		qui = qui + 1
	elif(v[i] == 6):
		sex = sex + 1
	elif (v[i] == 7):
		sab = sab + 1
s = seg + ter + qua + qui + sex + sab
t = zeros(6, dtype=float)
for i in v:
	t[0] = round((seg / s) * 100 , 1)
	t[1] = round((ter / s) * 100 , 1)
	t[2]= round((qua / s) * 100 , 1)
	t[3] = round((qui / s) * 100 , 1)
	t[4] = round((sex / s) * 100 , 1)
	t[5] = round((sab / s) * 100, 1)
print(t)


	
