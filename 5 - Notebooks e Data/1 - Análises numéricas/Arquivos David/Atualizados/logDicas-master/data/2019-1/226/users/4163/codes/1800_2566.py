from numpy import*

ft = array(eval(input("numero de faltas: ")))
pc = zeros(6, dtype=float)
for i in range(size(ft)):
	if ft[i]==2:
		pc[0]=pc[0]+1
	elif ft[i]==3 :
		pc[1] = pc[1]+1
	elif ft[i]== 4:
		pc[2] = pc[2]+1
	elif ft[i]== 5:
		pc[3] = pc[3]+1
	elif ft[i]== 6:
		pc[4] = pc[4]+1
	elif ft[i]== 7 :
		pc[5] = pc[5]+1		

for i in range(6):
	pc[i] = round(pc[i]/size(ft)*100, 1)
print(pc)