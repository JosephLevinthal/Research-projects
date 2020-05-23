from numpy import*
v= array(eval(input("insira as faltas da semana: ")))
n= zeros(6, dtype=float)

for i in range(size(v)):
	if(v[i]==2):
		n[0]=n[0]+1
	elif(v[i]==3):
		n[1]=n[1]+1
	elif(v[i]==4):
		n[2]=n[2]+1
	elif(v[i]==5):
		n[3]=n[3]+1
	elif(v[i]==6):
		n[4]=n[4]+1
	elif(v[i]==7):
		n[5]=n[5]+1
a=sum(n)
n= n*100
for j in range(size(n)):
	n[j]=round((n[j]/a),1)
print(n)
