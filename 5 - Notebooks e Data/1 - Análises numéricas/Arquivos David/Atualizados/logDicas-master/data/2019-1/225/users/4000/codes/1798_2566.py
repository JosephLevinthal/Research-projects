from numpy import*
v = array(eval(input("vetor faltas: ")))
s =0
t=0
qua = 0
qui = 0
sex = 0
sab = 0
for i in range(size(v)):
	if(v[i]==2):
		s = s + 1
	elif(v[i]==3):
		t= t + 1
	elif(v[i] ==4):
		qua = qua + 1
	elif(v[i]==5):
		qui = qui + 1
	elif(v[i] == 6):
		sex = sex + 1
	elif(v[i]==7):
		sab = sab +1
h = s + t + qua+ qui+sex+sab
j = zeros(6, dtype = float)
for i in range(size(j)):
	j[0] = round(((s/h)*100),1)
	j[1] = round(((t/h)*100),1)
	j[2] = round(((qua/h)*100),1)
	j[3] = round(((qui/h)*100),1)
	j[4] = round(((sex/h)*100),1)
	j[5] = round(((sab/h)*100),1)
print(j)
	
	

